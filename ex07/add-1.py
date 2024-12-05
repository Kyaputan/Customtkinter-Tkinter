import customtkinter as ctk
import os
from PIL import Image
import tkinter as tk
from tkinter import simpledialog

# Create main window
Start_window = ctk.CTk()

def setup_main_window():
    Start_window.title("Main Detection")

    screen_width = Start_window.winfo_screenwidth() / 2
    screen_height = Start_window.winfo_screenheight() / 2

    # Set window size to full screen
    Start_window.geometry(f"{screen_width}x{screen_height}")
    
    # Get image directory path
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
    
    # Load images
    logo_KMITL_image = ctk.CTkImage(Image.open(os.path.join(image_path, "KMITL-Photoroom.png")), size=(130, 130))
    logo_RIE_image = ctk.CTkImage(Image.open(os.path.join(image_path, "RIE-Photoroom.png")), size=(130, 130))
    
    # Logo frame
    logo_frame = ctk.CTkFrame(Start_window)
    logo_frame.pack(fill="x", pady=(0,10))

    navigation_frame_label_KMITL = ctk.CTkLabel(logo_frame, text="", image=logo_KMITL_image, font=ctk.CTkFont(size=16, weight="bold"),fg_color="white",corner_radius=20)
    navigation_frame_label_KMITL.pack(side="left", padx=20,pady=(10,10))

    logo_rie_label = ctk.CTkLabel(logo_frame, text="", image=logo_RIE_image,fg_color="white",corner_radius=20)
    logo_rie_label.pack(side="left",pady=(10,10))

    text_rie_label = ctk.CTkLabel(logo_frame, text="สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง วิทยาเขตชุมพรเขตรอุดมศักดิ์\nRobotics and Intelligent Electronics Engineering", 
                                font=ctk.CTkFont(size=16, weight="bold"), justify="left")
    text_rie_label.pack(side="left", padx=10,pady=(10,10))

    # Video frame container
    video_container = ctk.CTkFrame(Start_window)
    video_container.pack(fill="both", expand=True, pady=20)

    # Frame for the video content
    frame_c = ctk.CTkFrame(video_container, width=350, height=320, fg_color="white", corner_radius=10)
    frame_c.pack(side="top", expand=True, anchor="center", pady=(5, 10), padx=30)

    # Label with an image
    label_c = ctk.CTkLabel(frame_c, text="", image=logo_KMITL_image, width=300, height=310)
    label_c.pack(side="top", expand=True, pady=(10, 0))

    # Button
    button1 = ctk.CTkButton(frame_c, text="เปิดกล้อง 3")
    button1.pack(side="bottom", pady=(10, 10))


    # Menu frame
    menu_frame = ctk.CTkFrame(Start_window, height=100)
    menu_frame.pack(pady=5, fill="y", side="top", padx=10)

    # Add Camera Frames button
    add_camera_button = ctk.CTkButton(menu_frame, text="เพิ่มกล้อง", corner_radius=5, width=15, command=add_camera_frames)
    add_camera_button.pack(side="left", padx=10, pady=10)

    # Back button
    back_button = ctk.CTkButton(menu_frame, text="ย้อนกลับ", corner_radius=5, width=15)
    back_button.pack(side="left", padx=10, pady=10)

def add_camera_frames():
    num_frames = simpledialog.askinteger("เพิ่มกล้อง", "ใส่จำนวนกล้อง (1-4):", minvalue=1, maxvalue=4)


def start():
    setup_main_window()
    Start_window.mainloop()

start()