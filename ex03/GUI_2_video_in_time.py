import tkinter as tk
from tkinter import Label
import cv2
from PIL import Image, ImageTk

frame_width = 640
frame_height = 480

# ฟังก์ชันตรวจจับกรอบใบหน้า
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def on_exit():
    root.quit()


def detect_bounding_box(frame):
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return frame

def update_frames():
    for i, cap in enumerate(video_capture):
        ret, frame = cap.read()
        if ret:
            frame = detect_bounding_box(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (frame_width, frame_height))
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            labels[i].imgtk = imgtk
            labels[i].config(image=imgtk)
    root.after(10, update_frames)

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Live Video with Face Detection")

# แหล่งวิดีโอ
IP_camera = ['http://192.168.0.101:8080/video']
webcam_indexes = [0]
video_capture = []

# เชื่อมต่อ IP cameras
for url in IP_camera:
    cap = cv2.VideoCapture(url)
    if cap.isOpened():
        video_capture.append(cap)
    else:
        print(f"Failed to connect to IP camera at {url}")

# เชื่อมต่อ webcams
webcam_caps = [cv2.VideoCapture(index) for index in webcam_indexes]

# รวมแหล่งวิดีโอทั้งหมด
video_capture += webcam_caps

# สร้าง Labels สำหรับแสดงวิดีโอ
labels = [Label(root) for _ in video_capture]
for label in labels:
    label.pack(side="right", expand=True, fill="both")

exit_button = tk.Button(root, text="Exit", command=on_exit)
exit_button.pack(side=tk.BOTTOM, pady=20)
# อัพเดทเฟรมวิดีโอ
update_frames()

# เริ่มต้นแอปพลิเคชัน
root.mainloop()

# ปล่อยกล้องเมื่อปิดหน้าต่าง
for cap in video_capture:
    cap.release()
cv2.destroyAllWindows()
