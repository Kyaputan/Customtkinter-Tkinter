import tkinter as tk
from tkinter import Label
import cv2
from PIL import Image, ImageTk
from tkinter import messagebox

def on_exit():
    root.quit()

# ฟังก์ชันที่จะอัพเดทเฟรมจากกล้อง
def update_frame():
    ret, frame = cap.read()
    if ret:
        # แปลงสีภาพจาก BGR เป็น RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # แปลงภาพเป็น Image ของ PIL
        img = Image.fromarray(frame)
        # แปลงภาพเป็น ImageTk
        imgtk = ImageTk.PhotoImage(image=img)
        # อัพเดท Label ที่แสดงภาพ
        lbl_video.imgtk = imgtk
        lbl_video.config(image=imgtk)
    # เรียกฟังก์ชันนี้ใหม่ทุก ๆ 10 มิลลิวินาที
    lbl_video.after(100, update_frame)

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Live Video in Tkinter")

# สร้าง Label เพื่อแสดงวิดีโอ
lbl_video = Label(root)
lbl_video.pack()

# เริ่มต้นการจับภาพจากกล้อง (index 0 หมายถึงกล้องหลัก)
cap = cv2.VideoCapture(0)
exit_button = tk.Button(root, text="Exit", command=on_exit)
exit_button.pack(pady=10)
# เรียกฟังก์ชันอัพเดทเฟรมครั้งแรก
update_frame()

# เริ่มต้นแอปพลิเคชัน
root.mainloop()

# ปล่อยกล้องเมื่อปิดหน้าต่าง
cap.release()
cv2.destroyAllWindows()
