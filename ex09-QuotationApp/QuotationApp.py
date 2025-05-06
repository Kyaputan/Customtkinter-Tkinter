import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
import locale
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import cm
import os

# ตั้งค่าท้องถิ่นภาษาไทย
locale.setlocale(locale.LC_ALL, 'th_TH.UTF-8')

class QuotationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ระบบใบเสนอราคา")
        self.root.geometry("900x700")
        
        # ตัวแปรเก็บข้อมูล
        self.items = []
        self.item_id_counter = 1
        
        # เพิ่มตัวแปรสำหรับเก็บค่า VAT
        self.vat_enabled = tk.BooleanVar()
        self.vat_rate = 5  # VAT 5%
        
        self.create_fonts()
        self.create_widgets()
    
    def create_fonts(self):

        try:
            # ตรวจสอบฟอนต์ที่ใช้ได้กับภาษาไทย
            font_paths = [
                "THSarabun.ttf",
                "Tahoma.ttf",
                "Arial Unicode.ttf",
                "ArialUnicode.ttf",
                "Arial.ttf",
                "/usr/share/fonts/truetype/tlwg/Sarabun.ttf",
                "/usr/share/fonts/truetype/tlwg/Garuda.ttf",
                "/System/Library/Fonts/Thonburi.ttf",
                "CodeCit\Customtkinter-Tkinter\ex09-QuotationApp\THSarabunNew.ttf"
            ]

        
            for font_path in font_paths:
                try:
                    if os.path.exists(font_path):
                        font_name = os.path.basename(font_path).split('.')[0]
                        pdfmetrics.registerFont(TTFont(font_name, font_path))
                        print(f"ลงทะเบียนฟอนต์ {font_name} สำเร็จ")
                        self.thai_font_available = True
                        self.thai_font_name = font_name
                        break
                except:
                    continue
            
            # ถ้าไม่พบฟอนต์ไทย จะใช้ฟอนต์ดีฟอลต์
            if not self.thai_font_available:
                # ใช้ฟอนต์มาตรฐานของ ReportLab
                self.thai_font_name = "Helvetica"
                print(f"ไม่พบฟอนต์ไทย จะใช้ฟอนต์ {self.thai_font_name} แทน")
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการลงทะเบียนฟอนต์: {e}")
            self.thai_font_name = "Helvetica"
    
    def create_widgets(self):
        # สร้าง Notebook (Tab)
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Tab สำหรับสร้างใบเสนอราคา
        quotation_frame = ttk.Frame(notebook)
        notebook.add(quotation_frame, text="สร้างใบเสนอราคา")
        
        # Tab สำหรับตั้งค่าบริษัท
        company_frame = ttk.Frame(notebook)
        notebook.add(company_frame, text="ข้อมูลบริษัท")
        
        # สร้าง Widget สำหรับ Tab ใบเสนอราคา
        self.setup_quotation_tab(quotation_frame)
        
        # สร้าง Widget สำหรับ Tab ข้อมูลบริษัท
        self.setup_company_tab(company_frame)
    
    def setup_company_tab(self, parent):
        # กรอบข้อมูลบริษัท
        company_frame = ttk.LabelFrame(parent, text="ข้อมูลบริษัทผู้ออกใบเสนอราคา")
        company_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # ชื่อบริษัท
        ttk.Label(company_frame, text="ชื่อบริษัท:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.company_name = ttk.Entry(company_frame, width=50)
        self.company_name.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        self.company_name.insert(0, "บริษัท ตัวอย่าง จำกัด")
        
        # ที่อยู่บริษัท
        ttk.Label(company_frame, text="ที่อยู่:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.company_address = tk.Text(company_frame, width=50, height=3)
        self.company_address.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)
        self.company_address.insert("1.0", "123 ถนนตัวอย่าง แขวงตัวอย่าง เขตตัวอย่าง กรุงเทพฯ 10xxx")
        
        # เบอร์โทรศัพท์
        ttk.Label(company_frame, text="เบอร์โทรศัพท์:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.company_phone = ttk.Entry(company_frame, width=50)
        self.company_phone.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)
        self.company_phone.insert(0, "02-xxx-xxxx")
        
        # อีเมล
        ttk.Label(company_frame, text="อีเมล:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        self.company_email = ttk.Entry(company_frame, width=50)
        self.company_email.grid(row=3, column=1, sticky=tk.W, padx=10, pady=5)
        self.company_email.insert(0, "info@example.co.th")
        
        # เลขประจำตัวผู้เสียภาษี
        ttk.Label(company_frame, text="เลขประจำตัวผู้เสียภาษี:").grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        self.tax_id = ttk.Entry(company_frame, width=50)
        self.tax_id.grid(row=4, column=1, sticky=tk.W, padx=10, pady=5)
        self.tax_id.insert(0, "0-1234-56789-00-0")
        
        # โลโก้บริษัท (ถ้าต้องการ)
        ttk.Label(company_frame, text="โลโก้บริษัท (ถ้ามี):").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
        logo_frame = ttk.Frame(company_frame)
        logo_frame.grid(row=5, column=1, sticky=tk.W, padx=10, pady=5)
        
        self.logo_path = tk.StringVar()
        ttk.Entry(logo_frame, textvariable=self.logo_path, width=40).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(logo_frame, text="เลือกไฟล์", command=self.choose_logo).pack(side=tk.LEFT)
        
        # ปุ่มบันทึกข้อมูลบริษัท
        ttk.Button(company_frame, text="บันทึกข้อมูลบริษัท", command=self.save_company_info).grid(row=6, column=1, sticky=tk.E, padx=10, pady=20)
    
    def choose_logo(self):
        file_path = filedialog.askopenfilename(
            title="เลือกไฟล์โลโก้",
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg"), ("All files", "*.*")]
        )
        if file_path:
            self.logo_path.set(file_path)
    
    def save_company_info(self):
        messagebox.showinfo("บันทึกข้อมูล", "บันทึกข้อมูลบริษัทเรียบร้อยแล้ว")
    
    def setup_quotation_tab(self, parent):
        # Frame สำหรับข้อมูลหัวใบเสนอราคา
        header_frame = ttk.LabelFrame(parent, text="ข้อมูลใบเสนอราคา")
        header_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # แถวที่ 1: ชื่อลูกค้าและเลขที่เอกสาร
        ttk.Label(header_frame, text="ชื่อลูกค้า:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.customer_name = ttk.Entry(header_frame, width=40)
        self.customer_name.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        
        ttk.Label(header_frame, text="เลขที่เอกสาร:").grid(row=0, column=2, sticky=tk.W, padx=10, pady=5)
        self.doc_number = ttk.Entry(header_frame, width=20)
        self.doc_number.grid(row=0, column=3, sticky=tk.W, padx=10, pady=5)
        self.doc_number.insert(0, f"QT-{datetime.now().strftime('%Y%m%d')}-001")
        
        # แถวที่ 2: ที่อยู่ลูกค้าและวันที่
        ttk.Label(header_frame, text="ที่อยู่ลูกค้า:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        self.customer_address = tk.Text(header_frame, width=40, height=3)
        self.customer_address.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)
        
        ttk.Label(header_frame, text="วันที่:").grid(row=1, column=2, sticky=tk.W, padx=10, pady=5)
        self.date_var = tk.StringVar()
        self.date_var.set(datetime.now().strftime("%d/%m/%Y"))
        self.date_entry = ttk.Entry(header_frame, textvariable=self.date_var, width=20)
        self.date_entry.grid(row=1, column=3, sticky=tk.W, padx=10, pady=5)
        
        # แถวที่ 3: โทรศัพท์และอีเมลลูกค้า
        ttk.Label(header_frame, text="โทรศัพท์:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        self.customer_phone = ttk.Entry(header_frame, width=40)
        self.customer_phone.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)
        
        ttk.Label(header_frame, text="อีเมล:").grid(row=2, column=2, sticky=tk.W, padx=10, pady=5)
        self.customer_email = ttk.Entry(header_frame, width=20)
        self.customer_email.grid(row=2, column=3, sticky=tk.W, padx=10, pady=5)
        
        # Frame สำหรับเพิ่มรายการสินค้า
        item_frame = ttk.LabelFrame(parent, text="เพิ่มรายการสินค้า/บริการ")
        item_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # รายละเอียดสินค้า
        ttk.Label(item_frame, text="รายละเอียด:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        self.item_description = ttk.Entry(item_frame, width=40)
        self.item_description.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        
        # จำนวน
        ttk.Label(item_frame, text="จำนวน:").grid(row=0, column=2, sticky=tk.W, padx=10, pady=5)
        self.item_quantity = ttk.Entry(item_frame, width=10)
        self.item_quantity.grid(row=0, column=3, sticky=tk.W, padx=10, pady=5)
        
        # ราคาต่อหน่วย
        ttk.Label(item_frame, text="ราคาต่อหน่วย:").grid(row=0, column=4, sticky=tk.W, padx=10, pady=5)
        self.item_unit_price = ttk.Entry(item_frame, width=15)
        self.item_unit_price.grid(row=0, column=5, sticky=tk.W, padx=10, pady=5)
        
        # ปุ่มเพิ่มรายการ
        ttk.Button(item_frame, text="เพิ่มรายการ", command=self.add_item).grid(row=0, column=6, sticky=tk.W, padx=10, pady=5)
        
        # Frame สำหรับแสดงรายการที่เพิ่มแล้ว
        list_frame = ttk.LabelFrame(parent, text="รายการสินค้า/บริการ")
        list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # สร้าง Treeview สำหรับแสดงรายการ
        columns = ("id", "description", "quantity", "unit_price", "total")
        self.item_tree = ttk.Treeview(list_frame, columns=columns, show="headings", height=10)
        
        # กำหนดหัวตาราง
        self.item_tree.heading("id", text="ลำดับ")
        self.item_tree.heading("description", text="รายละเอียด")
        self.item_tree.heading("quantity", text="จำนวน")
        self.item_tree.heading("unit_price", text="ราคาต่อหน่วย")
        self.item_tree.heading("total", text="ราคารวม")
        
        # กำหนดความกว้างคอลัมน์
        self.item_tree.column("id", width=50, anchor=tk.CENTER)
        self.item_tree.column("description", width=300)
        self.item_tree.column("quantity", width=100, anchor=tk.CENTER)
        self.item_tree.column("unit_price", width=100, anchor=tk.E)
        self.item_tree.column("total", width=100, anchor=tk.E)
        
        # เพิ่ม scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.item_tree.yview)
        self.item_tree.configure(yscroll=scrollbar.set)
        
        # จัดวาง Treeview และ scrollbar
        self.item_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # เพิ่มเมนูคลิกขวาเพื่อลบรายการ
        self.item_tree.bind("<Button-3>", self.show_context_menu)
        
        # Frame สำหรับหมายเหตุและ VAT
        note_frame = ttk.LabelFrame(parent, text="หมายเหตุและภาษี")
        note_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # หมายเหตุ
        ttk.Label(note_frame, text="หมายเหตุ:").grid(row=0, column=0, sticky=tk.NW, padx=10, pady=5)
        self.note = tk.Text(note_frame, width=40, height=3)
        self.note.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)
        
        # คำนวณ VAT
        ttk.Checkbutton(note_frame, text=f"คำนวณภาษีมูลค่าเพิ่ม (VAT {self.vat_rate}%)", variable=self.vat_enabled).grid(row=0, column=2, sticky=tk.W, padx=10, pady=5)
        
        # Frame สำหรับปุ่มด้านล่าง
        button_frame = ttk.Frame(parent)
        button_frame.pack(fill=tk.X, padx=10, pady=20)
        
        # ปุ่มสร้าง PDF
        ttk.Button(button_frame, text="สร้างไฟล์ PDF", command=self.generate_pdf).pack(side=tk.LEFT, padx=10)
        
        # ปุ่มล้างข้อมูล
        ttk.Button(button_frame, text="ล้างข้อมูล", command=self.clear_data).pack(side=tk.LEFT, padx=10)
        
        # แสดงผลรวม
        self.summary_frame = ttk.LabelFrame(parent, text="สรุปยอดเงิน")
        self.summary_frame.pack(fill=tk.X, padx=10)
        
        # ผลรวม
        ttk.Label(self.summary_frame, text="รวมเป็นเงิน:").grid(row=0, column=0, sticky=tk.E, padx=10, pady=5)
        self.subtotal_var = tk.StringVar()
        self.subtotal_var.set("0.00")
        ttk.Label(self.summary_frame, textvariable=self.subtotal_var).grid(row=0, column=1, sticky=tk.E, padx=10, pady=5)
        ttk.Label(self.summary_frame, text="บาท").grid(row=0, column=2, sticky=tk.W, padx=10, pady=5)
        
        # VAT
        ttk.Label(self.summary_frame, text=f"ภาษีมูลค่าเพิ่ม {self.vat_rate}%:").grid(row=1, column=0, sticky=tk.E, padx=10, pady=5)
        self.vat_var = tk.StringVar()
        self.vat_var.set("0.00")
        ttk.Label(self.summary_frame, textvariable=self.vat_var).grid(row=1, column=1, sticky=tk.E, padx=10, pady=5)
        ttk.Label(self.summary_frame, text="บาท").grid(row=1, column=2, sticky=tk.W, padx=10, pady=5)
        
        # ยอดรวมสุทธิ
        ttk.Label(self.summary_frame, text="ยอดรวมสุทธิ:").grid(row=2, column=0, sticky=tk.E, padx=10, pady=5)
        self.total_var = tk.StringVar()
        self.total_var.set("0.00")
        ttk.Label(self.summary_frame, textvariable=self.total_var, font=("TkDefaultFont", 12, "bold")).grid(row=2, column=1, sticky=tk.E, padx=10, pady=5)
        ttk.Label(self.summary_frame, text="บาท").grid(row=2, column=2, sticky=tk.W, padx=10, pady=5)
    
    def show_context_menu(self, event):
        # สร้างเมนูคลิกขวา
        context_menu = tk.Menu(self.root, tearoff=0)
        context_menu.add_command(label="ลบรายการ", command=self.delete_selected_item)
        
        # แสดงเมนูที่ตำแหน่งเมาส์
        try:
            context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            context_menu.grab_release()
    
    def delete_selected_item(self):
        # หารายการที่เลือก
        selected_item = self.item_tree.selection()
        if not selected_item:
            return
        
        # ลบรายการจาก Treeview และ list
        item_id = self.item_tree.item(selected_item, "values")[0]
        self.item_tree.delete(selected_item)
        
        # ลบรายการจาก list items
        self.items = [item for item in self.items if item["id"] != int(item_id)]
        
        # อัพเดทสรุปยอดเงิน
        self.update_totals()
    
    def add_item(self):
        # ตรวจสอบข้อมูล
        description = self.item_description.get().strip()
        quantity_str = self.item_quantity.get().strip()
        unit_price_str = self.item_unit_price.get().strip()
        
        if not description:
            messagebox.showerror("ข้อผิดพลาด", "กรุณาระบุรายละเอียดสินค้า/บริการ")
            return
        
        try:
            quantity = float(quantity_str)
            if quantity <= 0:
                raise ValueError("จำนวนต้องมากกว่า 0")
        except ValueError:
            messagebox.showerror("ข้อผิดพลาด", "กรุณาระบุจำนวนที่ถูกต้อง")
            return
        
        try:
            unit_price = float(unit_price_str)
            if unit_price < 0:
                raise ValueError("ราคาต้องไม่ติดลบ")
        except ValueError:
            messagebox.showerror("ข้อผิดพลาด", "กรุณาระบุราคาต่อหน่วยที่ถูกต้อง")
            return
        
        # คำนวณราคารวม
        total_price = quantity * unit_price
        
        # เพิ่มข้อมูลลงใน list
        item = {
            "id": self.item_id_counter,
            "description": description,
            "quantity": quantity,
            "unit_price": unit_price,
            "total": total_price
        }
        self.items.append(item)
        
        # เพิ่มข้อมูลลงใน Treeview
        self.item_tree.insert("", tk.END, values=(
            self.item_id_counter,
            description,
            f"{quantity:,.2f}",
            f"{unit_price:,.2f}",
            f"{total_price:,.2f}"
        ))
        
        # เพิ่มลำดับ
        self.item_id_counter += 1
        
        # ล้างข้อมูลในช่องกรอก
        self.item_description.delete(0, tk.END)
        self.item_quantity.delete(0, tk.END)
        self.item_unit_price.delete(0, tk.END)
        
        # อัพเดทสรุปยอดเงิน
        self.update_totals()
    
    def update_totals(self):
        # คำนวณผลรวม
        subtotal = sum(item["total"] for item in self.items)
        
        # คำนวณ VAT ถ้าเลือก
        vat_amount = subtotal * (self.vat_rate / 100) if self.vat_enabled.get() else 0
        
        # คำนวณยอดรวมสุทธิ
        total = subtotal + vat_amount
        
        # อัพเดทตัวแปร
        self.subtotal_var.set(f"{subtotal:,.2f}")
        self.vat_var.set(f"{vat_amount:,.2f}")
        self.total_var.set(f"{total:,.2f}")
    
    def clear_data(self):
        # ล้างข้อมูลในช่องกรอก
        self.customer_name.delete(0, tk.END)
        self.customer_address.delete("1.0", tk.END)
        self.customer_phone.delete(0, tk.END)
        self.customer_email.delete(0, tk.END)
        self.note.delete("1.0", tk.END)
        
        # ล้างรายการทั้งหมด
        for item in self.item_tree.get_children():
            self.item_tree.delete(item)
        
        # รีเซ็ตตัวแปร
        self.items = []
        self.item_id_counter = 1
        
        # รีเซ็ตสรุปยอดเงิน
        self.update_totals()
        
        # รีเซ็ตเลขที่เอกสาร
        self.doc_number.delete(0, tk.END)
        self.doc_number.insert(0, f"QT-{datetime.now().strftime('%Y%m%d')}-001")
        
        # รีเซ็ตวันที่
        self.date_var.set(datetime.now().strftime("%d/%m/%Y"))
    
    def format_thai_baht(self, amount):
        # แปลงจำนวนเงินเป็นตัวอักษรภาษาไทย (ตัวอย่างอย่างง่าย)
        # ในกรณีจริงควรใช้ไลบรารีที่รองรับภาษาไทยเช่น bahttext
        return f"{amount:,.2f} บาท"
    
    def generate_pdf(self):
        # ตรวจสอบว่ามีรายการหรือไม่
        if not self.items:
            messagebox.showerror("ข้อผิดพลาด", "ไม่มีรายการสินค้า/บริการ")
            return
        
        # ตรวจสอบข้อมูลลูกค้า
        if not self.customer_name.get().strip():
            messagebox.showerror("ข้อผิดพลาด", "กรุณาระบุชื่อลูกค้า")
            return
        
        # เลือกตำแหน่งที่จะบันทึกไฟล์
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            initialfile=f"ใบเสนอราคา_{self.doc_number.get().replace('/', '-')}.pdf",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        
        if not file_path:
            return
        
        try:
            # สร้าง PDF
            doc = SimpleDocTemplate(
                file_path,
                pagesize=A4,
                leftMargin=1*cm,
                rightMargin=1*cm,
                topMargin=1*cm,
                bottomMargin=1*cm
            )
            
            # รายการที่จะแสดงใน PDF
            elements = []
            
            # สร้างสไตล์
            styles = getSampleStyleSheet()
            
            # เพิ่มสไตล์สำหรับภาษาไทย
            try:
                # ใช้ฟอนต์ที่รองรับภาษาไทย
                thai_style = ParagraphStyle(
                    'Thai',
                    parent=styles['Normal'],
                    fontName=self.thai_font_name,
                    fontSize=12,
                    wordWrap='CJK' # ช่วยให้ตัดคำภาษาไทยได้ดีขึ้น
                )
                thai_heading = ParagraphStyle(
                    'ThaiHeading',
                    parent=styles['Heading1'],
                    fontName=self.thai_font_name,
                    fontSize=16,
                    wordWrap='CJK'
                )
            except:
                # กรณีมีปัญหาใช้สไตล์มาตรฐาน
                thai_style = styles['Normal']
                thai_heading = styles['Normal']
            
            # ส่วนหัวเอกสาร
            # ใช้ข้อความธรรมดาแทน Paragraph ในส่วนที่มีปัญหา
            data = [
                ["ใบเสนอราคา (Quotation)", "", "", ""],
                ["", "", "เลขที่:", self.doc_number.get()],
                ["", "", "วันที่:", self.date_var.get()],
                [Paragraph(f"<b>{self.company_name.get()}</b>", thai_style), "", "", ""],
                [Paragraph(self.company_address.get("1.0", tk.END).strip(), thai_style), "", "", ""],
                [f"โทร: {self.company_phone.get()}", "", f"อีเมล: {self.company_email.get()}", ""],
                [f"เลขประจำตัวผู้เสียภาษี: {self.tax_id.get()}", "", "", ""],
                ["", "", "", ""],
                [Paragraph("<b>ลูกค้า:</b>", thai_style), "", "", ""],
                [Paragraph(f"{self.customer_name.get()}", thai_style), "", "", ""],
                [Paragraph(self.customer_address.get("1.0", tk.END).strip(), thai_style), "", "", ""],
                [f"โทร: {self.customer_phone.get()}", "", f"อีเมล: {self.customer_email.get()}", ""],
                ["", "", "", ""],
            ]
            
            # สร้างตารางส่วนหัว
            header_table = Table(data, colWidths=[doc.width/2, doc.width/6, doc.width/6, doc.width/6])
            header_table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'LEFT' ,),
                ('ALIGN', (0, 0), (0, 0), 'CENTER'),
                ('SPAN', (0, 0), (3, 0)),
                ('SPAN', (0, 3), (3, 3)),
                ('SPAN', (0, 4), (3, 4)),
                ('SPAN', (0, 8), (3, 8)),
                ('SPAN', (0, 9), (3, 9)),
                ('SPAN', (0, 10), (3, 10)),
                ('FONTSIZE', (0, 0), (0, 0), 16),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 20),
                ('TOPPADDING', (0, 8), (-1, 8), 10),
                ('FONTNAME', (0, 0), (0, 0), self.thai_font_name),
                ('FONTNAME', (0, 3), (0, 4), self.thai_font_name),
            ]))
            
            elements.append(header_table)
            elements.append(Spacer(1, 20))
            
            # สร้างตารางรายการสินค้า/บริการ
            items_data = [
                ["ลำดับ", "รายละเอียด", "จำนวน", "ราคาต่อหน่วย", "ราคารวม"]
            ]
            
            # เพิ่มรายการ
            for item in self.items:
                items_data.append([
                    str(item["id"]),
                    item["description"],
                    f"{item['quantity']:,.2f}",
                    f"{item['unit_price']:,.2f}",
                    f"{item['total']:,.2f}"
                ])
            
            # คำนวณผลรวม
            subtotal = sum(item["total"] for item in self.items)
            vat_amount = subtotal * (self.vat_rate / 100) if self.vat_enabled.get() else 0
            total = subtotal + vat_amount
            
            # เพิ่มแถวผลรวม
            items_data.append(["", "", "", "รวมเป็นเงิน", f"{subtotal:,.2f}"])
            
            if self.vat_enabled.get():
                items_data.append(["", "", "", f"ภาษีมูลค่าเพิ่ม {self.vat_rate}%", f"{vat_amount:,.2f}"])
            
            items_data.append(["", "", "", "ยอดรวมสุทธิ", f"{total:,.2f}"])
            
            # สร้างตารางรายการ
            col_widths = [doc.width/10, doc.width*0.4, doc.width/10, doc.width/10, doc.width/10]
            items_table = Table(items_data, colWidths=col_widths)
            
            # ตกแต่งตารางรายการ
            items_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), self.thai_font_name),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                ('GRID', (0, 0), (-1, -2), 1, colors.black),
                ('ALIGN', (0, 1), (0, -1), 'CENTER'),
                ('ALIGN', (2, 1), (4, -1), 'RIGHT'),
                ('SPAN', (0, -3), (2, -3)),
                ('SPAN', (0, -2), (2, -2)),
                ('SPAN', (0, -1), (2, -1)),
                ('FONTNAME', (3, -3), (4, -1), self.thai_font_name),
                ('LINEBELOW', (3, -1), (4, -1), 1, colors.black),
                ('LINEABOVE', (3, -1), (4, -1), 1, colors.black),
            ]))
            
            elements.append(items_table)
            elements.append(Spacer(1, 20))
            
            # เพิ่มส่วนหมายเหตุ
            note_text = self.note.get("1.0", tk.END).strip()
            if note_text:
                elements.append(Paragraph("<b>หมายเหตุ:</b>", thai_style))
                elements.append(Paragraph(note_text, thai_style))
                elements.append(Spacer(1, 20))
            
            # ส่วนลงนาม
            signature_data = [
                ["", "", "", ""],
                ["........................................", "", "........................................", ""],
                ["ผู้จัดทำ", "", "ผู้มีอำนาจลงนาม", ""],
                ["วันที่: ...../...../......", "", "วันที่: ...../...../......", ""],
                ["", "", "", ""],
                ["", "", "........................................", ""],
                ["", "", "ผู้รับใบเสนอราคา", ""],
                ["", "", "วันที่: ...../...../......", ""],
            ]
            
            signature_table = Table(signature_data, colWidths=[doc.width/4, doc.width/4, doc.width/4, doc.width/4])
            signature_table.setStyle(TableStyle([
                ('ALIGN', (0, 1), (0, 3), 'CENTER'),
                ('ALIGN', (2, 1), (2, 3), 'CENTER'),
                ('ALIGN', (2, 5), (2, 7), 'CENTER'),
                ('SPAN', (0, 1), (1, 1)),
                ('SPAN', (2, 1), (3, 1)),
                ('SPAN', (0, 2), (1, 2)),
                ('SPAN', (2, 2), (3, 2)),
                ('SPAN', (0, 3), (1, 3)),
                ('SPAN', (2, 3), (3, 3)),
                ('SPAN', (2, 5), (3, 5)),
                ('SPAN', (2, 6), (3, 6)),
                ('SPAN', (2, 7), (3, 7)),
            ]))
            
            elements.append(signature_table)
            
            # สร้าง PDF
            doc.build(elements)
            
            messagebox.showinfo("สำเร็จ", f"สร้างไฟล์ PDF สำเร็จแล้วที่:\n{file_path}")
            
        except Exception as e:
            messagebox.showerror("ข้อผิดพลาด", f"เกิดข้อผิดพลาดในการสร้างไฟล์ PDF:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuotationApp(root)
    root.mainloop()