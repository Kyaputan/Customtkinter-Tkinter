import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkcalendar import DateEntry
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
import os
import datetime
import json
from decimal import Decimal, ROUND_HALF_UP

# ลงทะเบียนฟอนต์ภาษาไทย
pdfmetrics.registerFont(TTFont('Thai', 'THSarabunNew.ttf'))

class QuotationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("แอปใบเสนอราคา")
        self.root.geometry("900x700")
        self.root.resizable(False, False)

        # ตัวแปรเก็บข้อมูล
        self.items = []
        self.item_id_counter = 1
        self.logo_path = ""
        self.vat_rate = 5  # VAT 5%
        self.vat_enabled = tk.BooleanVar(value=True)
        self.company_info = {
            "name": "บริษัท ตัวอย่าง จำกัด",
            "address": "123 ถนนตัวอย่าง แขวงตัวอย่าง เขตตัวอย่าง กรุงเทพฯ 10000",
            "phone": "02-123-4567",
            "email": "info@example.com",
            "tax_id": "0105558000000"
        }

        # UI
        self.create_widgets()
        
    def generate_pdf(self):
        if not self.items:
            messagebox.showerror("ข้อผิดพลาด", "ไม่มีรายการสินค้า")
            return

        filename = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="บันทึกไฟล์ PDF"
        )
        if not filename:
            return

        try:
            from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
            from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
            from reportlab.pdfbase import pdfmetrics
            from reportlab.pdfbase.ttfonts import TTFont
            from reportlab.lib.pagesizes import A4
            from reportlab.lib.units import cm
            from reportlab.lib import colors

            doc = SimpleDocTemplate(filename, pagesize=A4,
                                    leftMargin=2*cm, rightMargin=2*cm,
                                    topMargin=2*cm, bottomMargin=2*cm)
            elements = []

            # ลงทะเบียนฟอนต์ภาษาไทย
            thai_font = pdfmetrics.registerFont(TTFont('Thai', 'THSarabunNew.ttf'))

            styles = getSampleStyleSheet()
            thai_style = ParagraphStyle('Thai', parent=styles['Normal'], fontName=thai_font, fontSize=12)
            thai_heading = ParagraphStyle('ThaiHeading', parent=styles['Heading1'], fontName=thai_font, fontSize=16)

            # ส่วนหัวเอกสาร
            data = [
                [Paragraph("<b>ใบเสนอราคา</b>", thai_heading), "", "", ""],
                ["", "", "เลขที่:", self.doc_number.get()],
                ["", "", "วันที่:", self.date_var.get()],
                [Paragraph(f"<b>{self.company_name.get()}</b>", thai_style), "", "", ""],
                [Paragraph(self.company_address.get("1.0", tk.END).strip(), thai_style), "", "", ""],
                [f"โทร: {self.company_phone.get()}", "", f"อีเมล: {self.company_email.get()}", ""],
                [f"เลขประจำตัวผู้เสียภาษี: {self.tax_id.get()}", "", "", ""],
                ["", "", "", ""],
                [Paragraph("<b>ลูกค้า:</b>", thai_style), "", "", ""],
                [Paragraph(self.customer_name.get(), thai_style), "", "", ""],
                [Paragraph(self.customer_address.get("1.0", tk.END).strip(), thai_style), "", "", ""],
                [f"โทร: {self.customer_phone.get()}", "", f"อีเมล: {self.customer_email.get()}", ""],
                ["", "", "", ""],
            ]

            header_table = Table(data, colWidths=[doc.width/2, doc.width/6, doc.width/6, doc.width/6])
            header_table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('SPAN', (0, 0), (3, 0)),
                ('SPAN', (0, 3), (3, 3)),
                ('SPAN', (0, 4), (3, 4)),
                ('SPAN', (0, 8), (3, 8)),
                ('SPAN', (0, 9), (3, 9)),
                ('SPAN', (0, 10), (3, 10)),
                ('FONTSIZE', (0, 0), (0, 0), 16),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 20),
                ('TOPPADDING', (0, 8), (-1, 8), 10),
            ]))
            elements.append(header_table)
            elements.append(Spacer(1, 20))

            # ตารางรายการ
            items_data = [["ลำดับ", "รายละเอียด", "จำนวน", "ราคาต่อหน่วย", "ราคารวม"]]
            for item in self.items:
                items_data.append([
                    str(item["id"]),
                    item["description"],
                    f"{item['quantity']:,.2f}",
                    f"{item['unit_price']:,.2f}",
                    f"{item['total']:,.2f}"
                ])

            subtotal = sum(item["total"] for item in self.items)
            vat_amount = subtotal * (self.vat_rate / 100) if self.vat_enabled.get() else 0
            total = subtotal + vat_amount

            items_data.append(["", "", "", "รวมเป็นเงิน", f"{subtotal:,.2f}"])
            if self.vat_enabled.get():
                items_data.append(["", "", "", f"VAT {self.vat_rate}%", f"{vat_amount:,.2f}"])
            items_data.append(["", "", "", "ยอดรวมสุทธิ", f"{total:,.2f}"])

            items_table = Table(items_data, colWidths=[doc.width/10, doc.width*0.4, doc.width/10, doc.width/10, doc.width/10])
            items_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), thai_font),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),
                ('ALIGN', (2, 1), (4, -1), 'RIGHT'),
                ('SPAN', (0, -3), (3, -3)),
                ('SPAN', (0, -2), (3, -2)),
                ('SPAN', (0, -1), (3, -1)),
            ]))
            elements.append(items_table)
            elements.append(Spacer(1, 20))

            # หมายเหตุ
            note_text = self.note.get("1.0", tk.END).strip()
            if note_text:
                elements.append(Paragraph("<b>หมายเหตุ:</b>", thai_style))
                elements.append(Paragraph(note_text, thai_style))
                elements.append(Spacer(1, 20))

            # ส่วนเซ็นชื่อ
            signature_data = [
                ["", "", "", ""],
                ["........................................", "", "........................................", ""],
                ["ผู้จัดทำ", "", "ผู้รับใบเสนอราคา", ""],
                ["วันที่: ...../...../......", "", "วันที่: ...../...../......", ""],
                ["", "", "", ""],
            ]
            signature_table = Table(signature_data, colWidths=[doc.width/4]*4)
            signature_table.setStyle(TableStyle([
                ('ALIGN', (0, 1), (0, 3), 'CENTER'),
                ('ALIGN', (2, 1), (2, 3), 'CENTER'),
                ('SPAN', (0, 1), (1, 1)),
                ('SPAN', (2, 1), (3, 1)),
                ('SPAN', (0, 2), (1, 2)),
                ('SPAN', (2, 2), (3, 2)),
                ('SPAN', (0, 3), (1, 3)),
                ('SPAN', (2, 3), (3, 3)),
            ]))
            elements.append(signature_table)

            # สร้าง PDF
            doc.build(elements)
            messagebox.showinfo("สำเร็จ", f"สร้างไฟล์ PDF เรียบร้อยแล้ว:\n{filename}")

        except Exception as e:
            messagebox.showerror("ข้อผิดพลาด", f"เกิดข้อผิดพลาดในการสร้างไฟล์ PDF:\n{str(e)}")
    def create_widgets(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Tab: สร้างใบเสนอราคา
        quotation_tab = ttk.Frame(notebook)
        notebook.add(quotation_tab, text="สร้างใบเสนอราคา")

        # Tab: ข้อมูลบริษัท
        company_tab = ttk.Frame(notebook)
        notebook.add(company_tab, text="ข้อมูลบริษัท")

        self.setup_company_tab(company_tab)
        self.setup_quotation_tab(quotation_tab)

    def setup_company_tab(self, parent):
        frame = ttk.LabelFrame(parent, text="ข้อมูลบริษัท")
        frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame, text="ชื่อบริษัท").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.company_name = ttk.Entry(frame, width=50)
        self.company_name.grid(row=0, column=1, padx=5, pady=5)
        self.company_name.insert(0, self.company_info["name"])

        ttk.Label(frame, text="ที่อยู่").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.company_address = tk.Text(frame, height=3, width=50)
        self.company_address.grid(row=1, column=1, padx=5, pady=5)
        self.company_address.insert("1.0", self.company_info["address"])

        ttk.Label(frame, text="โทรศัพท์").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.company_phone = ttk.Entry(frame, width=50)
        self.company_phone.grid(row=2, column=1, padx=5, pady=5)
        self.company_phone.insert(0, self.company_info["phone"])

        ttk.Label(frame, text="อีเมล").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.company_email = ttk.Entry(frame, width=50)
        self.company_email.grid(row=3, column=1, padx=5, pady=5)
        self.company_email.insert(0, self.company_info["email"])

        ttk.Label(frame, text="เลขประจำตัวผู้เสียภาษี").grid(row=4, column=0, sticky="w", padx=5, pady=5)
        self.tax_id = ttk.Entry(frame, width=50)
        self.tax_id.grid(row=4, column=1, padx=5, pady=5)
        self.tax_id.insert(0, self.company_info["tax_id"])

        ttk.Label(frame, text="โลโก้บริษัท").grid(row=5, column=0, sticky="w", padx=5, pady=5)
        ttk.Button(frame, text="เลือกไฟล์", command=self.select_logo).grid(row=5, column=1, sticky="w", padx=5, pady=5)

        ttk.Button(frame, text="บันทึกข้อมูลบริษัท", command=self.save_company_info).grid(
            row=6, column=1, sticky="e", padx=5, pady=10)

    def select_logo(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        if path:
            self.logo_path = path

    def save_company_info(self):
        self.company_info.update({
            "name": self.company_name.get(),
            "address": self.company_address.get("1.0", "end-1c"),
            "phone": self.company_phone.get(),
            "email": self.company_email.get(),
            "tax_id": self.tax_id.get()
        })
        messagebox.showinfo("สำเร็จ", "บันทึกข้อมูลบริษัทเรียบร้อยแล้ว")

    def setup_quotation_tab(self, parent):
        # หัวข้อลูกค้า
        customer_frame = ttk.LabelFrame(parent, text="ข้อมูลลูกค้า")
        customer_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(customer_frame, text="ชื่อลูกค้า").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.customer_name = ttk.Entry(customer_frame, width=40)
        self.customer_name.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(customer_frame, text="ที่อยู่").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.customer_address = tk.Text(customer_frame, height=3, width=40)
        self.customer_address.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(customer_frame, text="เบอร์โทร").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.customer_phone = ttk.Entry(customer_frame, width=40)
        self.customer_phone.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(customer_frame, text="อีเมล").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.customer_email = ttk.Entry(customer_frame, width=40)
        self.customer_email.grid(row=3, column=1, padx=5, pady=5)

        # รายการสินค้า
        item_frame = ttk.LabelFrame(parent, text="เพิ่มรายการ")
        item_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(item_frame, text="รายละเอียด").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.item_desc = ttk.Entry(item_frame, width=40)
        self.item_desc.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(item_frame, text="จำนวน").grid(row=0, column=2, sticky="w", padx=5, pady=5)
        self.item_qty = ttk.Entry(item_frame, width=10)
        self.item_qty.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(item_frame, text="ราคาต่อหน่วย").grid(row=0, column=4, sticky="w", padx=5, pady=5)
        self.item_price = ttk.Entry(item_frame, width=10)
        self.item_price.grid(row=0, column=5, padx=5, pady=5)

        ttk.Button(item_frame, text="เพิ่มรายการ", command=self.add_item).grid(row=0, column=6, padx=5, pady=5)

        # ตารางรายการ
        tree_frame = ttk.Frame(parent)
        tree_frame.pack(fill="both", expand=True, padx=10, pady=5)

        cols = ("id", "desc", "qty", "price", "total")
        self.tree = ttk.Treeview(tree_frame, columns=cols, show="headings", height=10)
        self.tree.heading("id", text="ลำดับ")
        self.tree.heading("desc", text="รายละเอียด")
        self.tree.heading("qty", text="จำนวน")
        self.tree.heading("price", text="ราคาต่อหน่วย")
        self.tree.heading("total", text="ราคารวม")

        self.tree.column("id", width=50, anchor="center")
        self.tree.column("desc", width=300)
        self.tree.column("qty", width=80, anchor="center")
        self.tree.column("price", width=100, anchor="e")
        self.tree.column("total", width=100, anchor="e")

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # หมายเหตุ
        note_frame = ttk.Frame(parent)
        note_frame.pack(padx=10, pady=5, fill="x")
        ttk.Label(note_frame, text="หมายเหตุ").pack(anchor="w")
        self.note = tk.Text(note_frame, height=3)
        self.note.pack(fill="x", expand=True)

        # ปุ่ม
        button_frame = ttk.Frame(parent)
        button_frame.pack(pady=10)

        ttk.Checkbutton(button_frame, text=f"คำนวณ VAT {self.vat_rate}%", variable=self.vat_enabled).pack(side="left", padx=10)
        ttk.Button(button_frame, text="สร้าง PDF", command=self.generate_pdf).pack(side="left", padx=10)
        ttk.Button(button_frame, text="ล้างข้อมูล", command=self.clear_data).pack(side="left", padx=10)

    def add_item(self):
        desc = self.item_desc.get().strip()
        qty = self.item_qty.get().strip()
        price = self.item_price.get().strip()

        if not desc or not qty or not price:
            messagebox.showwarning("ข้อผิดพลาด", "กรุณากรอกข้อมูลให้ครบถ้วน")
            return

        try:
            qty = float(qty)
            price = float(price)
        except ValueError:
            messagebox.showerror("ข้อผิดพลาด", "จำนวนและราคาต้องเป็นตัวเลขเท่านั้น")
            return

        total = qty * price

        self.items.append({"id": self.item_id_counter, "desc": desc, "qty": qty, "price": price, "total": total})
        self.tree.insert("", "end", values=(self.item_id_counter, desc, f"{qty:.2f}", f"{price:.2f}", f"{total:.2f}"))
        self.item_id_counter += 1

        self.item_desc.delete(0, "end")
        self.item_qty.delete(0, "end")
        self.item_price.delete(0, "end")

    def clear_data(self):
        self.tree.delete(*self.tree.get_children())
        self.items.clear()
        self.item_id_counter = 1
        self.customer_name.delete(0, "end")
        self.customer_address.delete("1.0", "end")
        self.customer_phone.delete(0, "end")
        self.customer_email.delete(0, "end")
        self.note.delete("1.0", "end")


        
if __name__ == "__main__":
    root = tk.Tk()
    app = QuotationApp(root)
    root.mainloop()