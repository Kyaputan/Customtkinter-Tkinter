import customtkinter as ctk
from PIL import Image, ImageTk
import cv2
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from ultralytics import YOLO
import os

folder_path = os.path.dirname(os.path.realpath(__file__))
model_path = os.path.join(folder_path, "modelYolo.onnx")
model = YOLO(model_path,task="detect")

def load_image(filepath):
    global img_display, img_path  
    img = cv2.imread(filepath)
    if img is not None:
        small_frame = cv2.resize(img, (640, 640))
        img = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        img_display = Image.fromarray(img)
        img_display = ImageTk.PhotoImage(img_display)
        label.configure(image=img_display)
        label.image = img_display  # เก็บอ้างอิงเพื่อไม่ให้ภาพถูกลบ
        img_path = filepath  # เก็บ path ของรูปภาพ
    else:
        showinfo(title="Error", message="Could not load image")

def select_file():
    filetypes = (('Image files', '*.jpg;*.jpeg;*.png'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open an image file', initialdir='/', filetypes=filetypes)
    
    if filename:  
        load_image(filename)

def detect_yolo(frame):

    results = model.predict(frame,conf=0.2)
    processed_image = results[0].plot()
    return processed_image


def process_yolo():
    if img_path:
        img_yolo = detect_yolo(img_path)

        # ตรวจสอบว่าผลลัพธ์ไม่เป็น None
        if img_yolo is not None:
            img_yolo = cv2.resize(img_yolo, (640, 640))
            img_yolo = cv2.cvtColor(img_yolo, cv2.COLOR_BGR2RGB)
            img_yolo = Image.fromarray(img_yolo)
            img_yolo = ImageTk.PhotoImage(img_yolo)

            # อัปเดตภาพใน Label
            label.configure(image=img_yolo)
            label.image = img_yolo  # เก็บอ้างอิงไม่ให้ภาพถูกลบ
        else:
            showinfo(title="Error", message="Could not process image with YOLO")
    else:
        showinfo(title="Error", message="Please select an image first")


# สร้างหน้าต่างหลัก
app = ctk.CTk()
app.geometry("800x600")
app.title("CustomTkinter with YOLO Image Processing")

# พื้นที่แสดงภาพหรือวิดีโอ
frame_image = ctk.CTkFrame(app)
frame_image.pack(pady=20, padx=20, expand=True, fill="both")

# Label สำหรับแสดงภาพ
label = ctk.CTkLabel(frame_image, text="")
label.pack(expand=True)

# สร้างกรอบปุ่มด้านล่าง
frame_buttons = ctk.CTkFrame(app)
frame_buttons.pack(pady=10)

# ปุ่มเลือกไฟล์
button1 = ctk.CTkButton(frame_buttons, text="เลือกรูปภาพ", command=select_file)
button1.pack(side="left", padx=10)

# ปุ่มประมวลผลด้วย YOLO
button2 = ctk.CTkButton(frame_buttons, text="ประมวลผล YOLO", command=process_yolo)
button2.pack(side="right", padx=10)


img_path = None 
app.mainloop()
