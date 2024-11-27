import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
import os
import threading

img_count = 0
cap_b = None

# ฟังก์ชันเปิดกล้อง B
def open_camera_b():
    global cap_b
    cap_b = cv2.VideoCapture(0)  # สมมติว่ากล้อง B คือกล้องที่ 1
    threading.Thread(target=update_camera_b).start()  # เรียกใช้ฟังก์ชันในเธรดแยก

# ฟังก์ชันอัปเดตภาพจากกล้อง B
def update_camera_b():
    global cap_b
    while cap_b.isOpened():
        ret, frame = cap_b.read()
        if ret:
            # แปลงภาพจาก OpenCV (BGR) เป็นรูปแบบที่ tkinter ใช้ได้ (RGB)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            label_b.imgtk = imgtk
            label_b.configure(image=imgtk)
        cv2.waitKey(10)

# ฟังก์ชันนับถอยหลังและบันทึกภาพ
def countdown_and_save():
    countdown(5)  # เริ่มนับถอยหลังจาก 5 วินาที

# ฟังก์ชันสำหรับนับถอยหลัง
def countdown(count):
    if count > 0:
        label_b.configure(text=f"Saving in {count}...")  # แสดงข้อความนับถอยหลัง
        label_b.after(1000, countdown, count - 1)  # เรียกใช้งาน countdown อีกครั้งหลังจาก 1 วินาที
    else:
        save_image_b()  # เรียกใช้ฟังก์ชันบันทึกภาพเมื่อถึง 0

# ฟังก์ชันบันทึกภาพจากกล้อง B
def save_image_b():
    global img_count
    if cap_b is not None and cap_b.isOpened():
        ret, frame = cap_b.read()
        if ret:
            filename = entry_name.get()  # รับชื่อจากช่องกรอกชื่อ
            if filename:  # ตรวจสอบว่าชื่อไม่ว่าง
                save_path = "CodeCit/Lab5 Customtkinter&Tkinter/ex05/save"
                if not os.path.exists(save_path):
                    os.makedirs(save_path)  # สร้างโฟลเดอร์ถ้ายังไม่มี
                img_count += 1
                full_filename = os.path.join(save_path, f"{filename}.jpg")
                cv2.imwrite(full_filename, frame)
                print(f"ภาพถูกบันทึกไว้ที่: {full_filename}")
                label_b.configure(text="Image saved!")
            else:
                label_b.configure(text="Please enter a name!")

# ฟังก์ชันลบไฟล์ที่มีชื่อเดียวกัน
def delete_image():
    filename = entry_name.get()  # รับชื่อจากช่องกรอกชื่อ
    if filename:
        for ext in ['.jpg', '.jpeg']:
            file_path = os.path.join("CodeCit/Lab5 Customtkinter&Tkinter/ex05/save", f"{filename}{ext}")
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Deleted: {file_path}")
                label_b.configure(text=f"Deleted: {file_path}")
                return
        label_b.configure(text="File not found.")
    else:
        label_b.configure(text="Please enter a name!")

# ฟังก์ชันปิดกล้อง B
def close_camera_b():
    global cap_b
    if cap_b is not None and cap_b.isOpened():
        cap_b.release()
        label_b.configure(image='')  # ลบภาพใน label
        label_b.configure(text="Camera B Feed")  # คืนค่าข้อความเดิม

# สร้างหน้าต่างหลักของ customtkinter
root = ctk.CTk()
root.geometry("800x600")

# ช่องกรอกชื่อ
entry_name = ctk.CTkEntry(root, placeholder_text="Enter image name")
entry_name.pack(pady=10)

# ปุ่มเปิดกล้อง B
btn_open_b = ctk.CTkButton(root, text="Open Camera B", command=open_camera_b)
btn_open_b.pack(pady=10)

# ปุ่มบันทึกภาพจากกล้อง B
btn_save_b = ctk.CTkButton(root, text="Save Image", command=countdown_and_save)
btn_save_b.pack(pady=10)

# ปุ่มลบไฟล์ที่มีชื่อเดียวกัน
btn_delete_b = ctk.CTkButton(root, text="Delete Image", command=delete_image)
btn_delete_b.pack(pady=10)

# ปุ่มปิดกล้อง B
btn_close_b = ctk.CTkButton(root, text="Close Camera B", command=close_camera_b)
btn_close_b.pack(pady=10)

# Label สำหรับแสดงฟีดจากกล้อง B
label_b = ctk.CTkLabel(root, text="Camera B Feed")
label_b.pack(pady=20)

# รัน tkinter loop
root.mainloop()
