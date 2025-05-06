import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from fpdf import FPDF
import json
import datetime
import os

DATA_FILE = "data.json"


def load_data():
    """Load saved data from JSON file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print("Error loading data:", e)
            return {"customers": {}}
    else:
        return {"customers": {}}


def save_data(data):
    """Save data to JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Error saving data:", e)



# โหลดข้อมูลเมื่อเริ่มโปรแกรม
data = load_data()


def generate_pdf():
    """Generate the quotation PDF using fpdf."""
    # ดึงข้อมูลจากฟอร์ม
    company_name = company_name_var.get()
    company_address = company_address_var.get()
    company_phone = company_phone_var.get()
    company_email = company_email_var.get()
    logo_path = logo_path_var.get()

    customer_name = customer_name_var.get()
    doc_no = doc_no_var.get()
    date = date_var.get()
    note = note_text.get("1.0", tk.END).strip()

    # ตรวจสอบว่ามีรายการอย่างน้อยหนึ่งรายการ
    if not items:
        messagebox.showwarning("ไม่มีรายการ", "กรุณาเพิ่มรายการสินค้าอย่างน้อยหนึ่งรายการ")
        return

    # สร้าง PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # แทรกโลโก้บริษัทหากมี
    if logo_path and os.path.exists(logo_path):
        try:
            pdf.image(logo_path, x=10, y=8, w=30)
        except Exception as e:
            print("Error adding logo:", e)

    # ข้อมูลบริษัท (เลื่อนตำแหน่งถ้ามีโลโก้)
    pdf.set_font("Arial", size=12)
    if logo_path:
        pdf.set_xy(50, 10)
    pdf.multi_cell(
        0,
        10,
        f"บริษัท: {company_name}\nที่อยู่: {company_address}\nโทร: {company_phone}\nอีเมล: {company_email}",
        align='L',
    )

    # หัวเรื่อง
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "ใบเสนอราคา (Quotation)", ln=True, align="C")
    pdf.ln(5)

    # ข้อมูลลูกค้า
    pdf.set_font("Arial", size=12)
    pdf.cell(40, 10, f"ลูกค้า: {customer_name}", ln=0)
    pdf.cell(60, 10, f"วันที่: {date}", ln=1)
    pdf.cell(40, 10, f"เลขที่เอกสาร: {doc_no}", ln=1)
    pdf.ln(5)

    # หัวตารางรายการสินค้า
    pdf.set_font("Arial", "B", 12)
    pdf.cell(10, 8, "ID", border=1, align="C")
    pdf.cell(80, 8, "รายละเอียด", border=1, align="C")
    pdf.cell(20, 8, "จำนวน", border=1, align="C")
    pdf.cell(30, 8, "ราคาต่อหน่วย", border=1, align="C")
    pdf.cell(30, 8, "รวม", border=1, align="C")
    pdf.ln()

    # รายการสินค้าแต่ละแถว
    pdf.set_font("Arial", size=12)
    total_sum = 0
    for idx, item in enumerate(items, start=1):
        desc = item["desc"]
        qty = item["qty"]
        price = item["unit_price"]
        total = qty * price
        total_sum += total
        pdf.cell(10, 8, str(idx), border=1, align="C")
        pdf.cell(80, 8, desc, border=1, align="L")
        pdf.cell(20, 8, str(qty), border=1, align="C")
        pdf.cell(30, 8, f"{price:.2f}", border=1, align="R")
        pdf.cell(30, 8, f"{total:.2f}", border=1, align="R")
        pdf.ln()

    # สรุปรวมยอด
    pdf.set_font("Arial", "B", 12)
    pdf.cell(140, 8, "รวมเป็นเงิน", border=1)
    pdf.cell(30, 8, f"{total_sum:.2f}", border=1, align="R")
    pdf.ln()
    vat_amount = 0
    # คำนวณ VAT ถ้าติ๊กเลือก
    if vat_var.get():
        vat_amount = total_sum * 0.05
        pdf.cell(140, 8, "VAT 5%", border=1)
        pdf.cell(30, 8, f"{vat_amount:.2f}", border=1, align="R")
        pdf.ln()
    grand_total = total_sum + vat_amount
    pdf.cell(140, 8, "จำนวนเงินรวมทั้งสิ้น", border=1)
    pdf.cell(30, 8, f"{grand_total:.2f}", border=1, align="R")
    pdf.ln(15)

    # หมายเหตุ (ถ้ามี)
    if note:
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 8, f"หมายเหตุ: {note}")

    # บันทึกไฟล์ PDF
    file_name = f"Quotation_{customer_name.replace(' ', '_')}_{date}.pdf"
    try:
        pdf.output(file_name)
        messagebox.showinfo("สำเร็จ", f"สร้างไฟล์ PDF เรียบร้อย: {file_name}")
    except Exception as e:
        messagebox.showerror("ข้อผิดพลาด", f"ไม่สามารถสร้างไฟล์ PDF ได้: {e}")

    # บันทึกข้อมูลลูกค้าและรายการลงไฟล์ JSON
    if customer_name:
        data.setdefault("customers", {})
        data["customers"][customer_name] = {"items": items.copy()}
        save_data(data)


def clear_data():
    """Clear all input fields and item list."""
    # ล้างข้อมูลบริษัท
    company_name_var.set("")
    company_address_var.set("")
    company_phone_var.set("")
    company_email_var.set("")
    logo_path_var.set("")
    # ล้างข้อมูลลูกค้า
    customer_name_var.set("")
    doc_no_var.set("")
    date_var.set("")
    note_text.delete("1.0", tk.END)
    # ล้างข้อมูลรายการสินค้าในฟอร์ม
    desc_var.set("")
    qty_var.set("")
    price_var.set("")
    # ล้างตารางรายการสินค้า
    for row in tree.get_children():
        tree.delete(row)
    items.clear()
    # รีเซ็ต VAT
    vat_var.set(False)


root = tk.Tk()
root.title("โปรแกรมใบเสนอราคา")

# --- ข้อมูลบริษัท ---
frame_company = ttk.LabelFrame(root, text="ข้อมูลบริษัท")
frame_company.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

tk.Label(frame_company, text="ชื่อบริษัท:").grid(row=0, column=0, sticky="e")
company_name_var = tk.StringVar()
tk.Entry(frame_company, textvariable=company_name_var, width=40).grid(
    row=0, column=1, padx=5, pady=2
)

tk.Label(frame_company, text="ที่อยู่บริษัท:").grid(row=1, column=0, sticky="e")
company_address_var = tk.StringVar()
tk.Entry(frame_company, textvariable=company_address_var, width=40).grid(
    row=1, column=1, padx=5, pady=2
)

tk.Label(frame_company, text="เบอร์ติดต่อ:").grid(row=2, column=0, sticky="e")
company_phone_var = tk.StringVar()
tk.Entry(frame_company, textvariable=company_phone_var, width=40).grid(
    row=2, column=1, padx=5, pady=2
)

tk.Label(frame_company, text="อีเมลบริษัท:").grid(row=3, column=0, sticky="e")
company_email_var = tk.StringVar()
tk.Entry(frame_company, textvariable=company_email_var, width=40).grid(
    row=3, column=1, padx=5, pady=2
)

tk.Label(frame_company, text="โลโก้บริษัท:").grid(row=4, column=0, sticky="e")
logo_path_var = tk.StringVar()
tk.Entry(frame_company, textvariable=logo_path_var, width=30).grid(
    row=4, column=1, padx=5, pady=2, sticky="w"
)
tk.Button(
    frame_company,
    text="Browse",
    command=lambda: logo_path_var.set(
        filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.gif")])
    ),
).grid(row=4, column=2, padx=5)
# --- ข้อมูลลูกค้า ---
frame_customer = ttk.LabelFrame(root, text="ข้อมูลลูกค้า")
frame_customer.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

tk.Label(frame_customer, text="ชื่อลูกค้า:").grid(row=0, column=0, sticky="e")
customer_name_var = tk.StringVar()
tk.Entry(frame_customer, textvariable=customer_name_var, width=30).grid(
    row=0, column=1, padx=5, pady=2, sticky="w"
)

tk.Label(frame_customer, text="เลขที่เอกสาร:").grid(row=0, column=2, sticky="e")
doc_no_var = tk.StringVar()
tk.Entry(frame_customer, textvariable=doc_no_var, width=15).grid(
    row=0, column=3, padx=5, pady=2, sticky="w"
)

tk.Label(frame_customer, text="วันที่:").grid(row=1, column=0, sticky="e")
date_var = tk.StringVar(value=str(datetime.date.today()))
tk.Entry(frame_customer, textvariable=date_var, width=15).grid(
    row=1, column=1, padx=5, pady=2, sticky="w"
)

tk.Label(frame_customer, text="หมายเหตุ:").grid(row=2, column=0, sticky="ne")
note_text = tk.Text(frame_customer, width=50, height=3)
note_text.grid(row=2, column=1, columnspan=3, padx=5, pady=2, sticky="w")

# Combobox เลือกลูกค้าเก่า (หากมีข้อมูลบันทึก)
tk.Label(frame_customer, text="เลือกลูกค้าเก่า:").grid(row=1, column=2, sticky="e")
customer_names = list(data.get("customers", {}).keys())
customer_combo = ttk.Combobox(frame_customer, values=customer_names, state="readonly")
customer_combo.grid(row=1, column=3, padx=5, pady=2, sticky="w")


# ฟังก์ชันโหลดลูกค้าเก่ามาแสดงรายการ
def load_customer(event):
    name = customer_combo.get()
    if name and name in data.get("customers", {}):
        cust = data["customers"][name]
        customer_name_var.set(name)
        # ล้างรายการเดิม
        for row in tree.get_children():
            tree.delete(row)
        items.clear()
        # โหลดรายการสินค้าเก่า
        for idx, item in enumerate(cust.get("items", []), start=1):
            items.append(item)
            total = item["qty"] * item["unit_price"]
            tree.insert(
                "",
                "end",
                values=(idx, item["desc"], item["qty"], item["unit_price"], total),
            )


customer_combo.bind("<<ComboboxSelected>>", load_customer)
# --- ระบบรายการสินค้า ---
frame_product = ttk.LabelFrame(root, text="รายการสินค้า")
frame_product.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

tk.Label(frame_product, text="รายละเอียด:").grid(row=0, column=0, sticky="e")
desc_var = tk.StringVar()
tk.Entry(frame_product, textvariable=desc_var, width=30).grid(
    row=0, column=1, padx=5, pady=2
)

tk.Label(frame_product, text="จำนวน:").grid(row=0, column=2, sticky="e")
qty_var = tk.StringVar()
tk.Entry(frame_product, textvariable=qty_var, width=10).grid(
    row=0, column=3, padx=5, pady=2
)

tk.Label(frame_product, text="ราคาต่อหน่วย:").grid(row=0, column=4, sticky="e")
price_var = tk.StringVar()
tk.Entry(frame_product, textvariable=price_var, width=15).grid(
    row=0, column=5, padx=5, pady=2
)

tk.Button(frame_product, text="เพิ่มรายการ", command=lambda: add_item()).grid(
    row=0, column=6, padx=5, pady=2
)

# ติ๊ก VAT 5%
vat_var = tk.BooleanVar()
tk.Checkbutton(frame_product, text="คำนวณ VAT 5%", variable=vat_var).grid(
    row=0, column=7, padx=10
)
# Treeview แสดงรายการสินค้า
tree = ttk.Treeview(
    root,
    columns=("ID", "Description", "Quantity", "UnitPrice", "Total"),
    show="headings",
)
tree.heading("ID", text="ID")
tree.heading("Description", text="รายละเอียด")
tree.heading("Quantity", text="จำนวน")
tree.heading("UnitPrice", text="ราคาต่อหน่วย")
tree.heading("Total", text="รวม")
tree.column("ID", width=30)
tree.column("Description", width=200)
tree.column("Quantity", width=60)
tree.column("UnitPrice", width=80)
tree.column("Total", width=80)
tree.grid(row=3, column=0, padx=10, pady=5, sticky="nsew")

# Scrollbar สำหรับตาราง
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=3, column=1, sticky="ns")

# ลิสต์เก็บรายการสินค้า
items = []


def add_item():
    """Add an item to the list and display in the table."""
    desc = desc_var.get()
    try:
        qty = float(qty_var.get())
        price = float(price_var.get())
    except ValueError:
        messagebox.showwarning("ข้อมูลไม่ถูกต้อง", "กรุณากรอกจำนวนและราคาเป็นตัวเลข")
        return
    if not desc or qty <= 0 or price < 0:
        messagebox.showwarning("ข้อมูลไม่สมบูรณ์", "กรุณากรอกข้อมูลสินค้าให้ครบถ้วน")
        return
    total = qty * price
    item = {"desc": desc, "qty": qty, "unit_price": price}
    items.append(item)
    # แสดงในตาราง
    tree.insert("", "end", values=(len(items), desc, qty, price, total))
    # ล้างช่องกรอกสินค้า
    desc_var.set("")
    qty_var.set("")
    price_var.set("")


# --- ปุ่มคำสั่งหลัก ---
btn_frame = tk.Frame(root)
btn_frame.grid(row=4, column=0, pady=10)
tk.Button(btn_frame, text="สร้าง PDF", command=generate_pdf).grid(
    row=0, column=0, padx=5
)
tk.Button(btn_frame, text="ล้างข้อมูล", command=clear_data).grid(row=0, column=1, padx=5)
root.mainloop()
