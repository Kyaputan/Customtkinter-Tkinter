from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors

def create_quotation_pdf(filename, app):
    doc = SimpleDocTemplate(filename, pagesize=A4, leftMargin=2*cm, rightMargin=2*cm,
                             topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    elements = []

    # ลงทะเบียนฟอนต์ภาษาไทย
    pdfmetrics.registerFont(TTFont('Thai', 'THSarabunNew.ttf'))
    thai_style = ParagraphStyle('thai', parent=styles['Normal'], fontName='Thai', fontSize=12)

    # ส่วนหัว
    elements.append(Paragraph("<b>ใบเสนอราคา</b>", thai_style))
    elements.append(Spacer(1, 12))

    # ข้อมูลบริษัท
    elements.append(Paragraph(f"<b>บริษัท:</b> {app.company_info['name']}", thai_style))
    elements.append(Paragraph(f"<b>ที่อยู่:</b> {app.company_info['address']}", thai_style))
    elements.append(Paragraph(f"<b>โทรศัพท์:</b> {app.company_info['phone']}", thai_style))
    elements.append(Paragraph(f"<b>Email:</b> {app.company_info['email']}", thai_style))
    elements.append(Paragraph(f"<b>เลขภาษี:</b> {app.company_info['tax_id']}", thai_style))
    elements.append(Spacer(1, 12))

    # ข้อมูลลูกค้า
    elements.append(Paragraph(f"<b>ชื่อลูกค้า:</b> {app.customer_name.get()}", thai_style))
    elements.append(Paragraph(f"<b>ที่อยู่:</b> {app.customer_address.get('1.0', 'end-1c')}", thai_style))
    elements.append(Paragraph(f"<b>โทรศัพท์:</b> {app.customer_phone.get()}", thai_style))
    elements.append(Paragraph(f"<b>Email:</b> {app.customer_email.get()}", thai_style))
    elements.append(Spacer(1, 12))

    # ตารางสินค้า
    data = [["ลำดับ", "รายละเอียด", "จำนวน", "ราคาต่อหน่วย", "ราคารวม"]]
    for item in app.items:
        data.append([item['id'], item['desc'], f"{item['qty']:.2f}", f"{item['price']:.2f}", f"{item['total']:.2f}"])

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    elements.append(table)

    # สร้าง PDF
    doc.build(elements)