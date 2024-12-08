import customtkinter as ctk
import os
from PIL import Image
import tkinter as tk

# Create main window
Start_window = ctk.CTk()


def start():

    Start_window.title("Main Detection")

    screen_width = Start_window.winfo_screenwidth() / 2
    screen_height = Start_window.winfo_screenheight() / 2

    # Set window size to full screen
    Start_window.geometry(f"{screen_width}x{screen_height}")

    # Get image directory path
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

    # Load two images
    logo_KMITL_image = ctk.CTkImage(
        Image.open(os.path.join(image_path, "KMITL-Photoroom.png")), size=(130, 130)
    )
    logo_RIE_image = ctk.CTkImage(
        Image.open(os.path.join(image_path, "RIE-Photoroom.png")), size=(130, 130)
    )
    logo_BG_image = ctk.CTkImage(
        Image.open(os.path.join(image_path, "bg_gradient.jpg")),
        size=(screen_width * 2, screen_height * 2),
    )

    # Background image
    bg_image_label = ctk.CTkLabel(Start_window, text="", image=logo_BG_image)
    bg_image_label.place(
        relx=0, rely=0, relwidth=1, relheight=1
    )  # Fill the entire window
    # Lower the background image to be behind other widgets
    bg_image_label.lower()

    # Configure logo frame
    logo_frame = ctk.CTkFrame(Start_window)
    logo_frame.pack(
        fill="x", pady=(0, 10)
    )  # Centering the frame horizontally with some padding

    navigation_frame_label_KMITL = ctk.CTkLabel(
        logo_frame,
        text="",
        image=logo_KMITL_image,
        font=ctk.CTkFont(size=16, weight="bold"),
        fg_color="white",
        corner_radius=20,
    )
    navigation_frame_label_KMITL.pack(side="left", padx=20, pady=(10, 10))

    logo_rie_label = ctk.CTkLabel(
        logo_frame, text="", image=logo_RIE_image, fg_color="white", corner_radius=20
    )
    logo_rie_label.pack(side="left", pady=(10, 10))

    # Create the label for the text (separate from the logo)
    text_rie_label = ctk.CTkLabel(
        logo_frame,
        text="สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง วิทยาเขตชุมพรเขตรอุดมศักดิ์\nRobotics and Intelligent Electronics Engineering",
        font=ctk.CTkFont(size=16, weight="bold"),
        justify="left",
    )
    text_rie_label.pack(side="left", padx=10, pady=(10, 10))

    # Video frame
    video_frame = ctk.CTkFrame(Start_window)
    video_frame.pack(fill="y", pady=10)  # Fill the remaining space

    frame_a = ctk.CTkFrame(
        video_frame, width=320, height=320, fg_color="white", corner_radius=20
    )
    frame_a.pack(side="left", expand=True, anchor="n", pady=(5, 10), padx=(30, 100))
    label_a = ctk.CTkLabel(
        frame_a, text="", image=logo_KMITL_image, width=320, height=320
    )
    label_a.pack(side="top", expand=True, padx=10)  # Expand to fill remaining space
    button1 = ctk.CTkButton(frame_a, text="เปิดกล้อง 1")
    button1.pack(side="bottom")

    frame_b = ctk.CTkFrame(
        video_frame, width=320, height=320, fg_color="white", corner_radius=20
    )
    frame_b.pack(side="right", expand=True, anchor="n", pady=(5, 10), padx=(100, 30))
    label_b = ctk.CTkLabel(
        frame_b, text="", image=logo_KMITL_image, width=320, height=320
    )
    label_b.pack(
        side="top", expand=True, padx=10
    )  # Split the space for both video labels
    buttonb = ctk.CTkButton(frame_b, text="เปิดกล้อง 2")
    buttonb.pack(side="bottom")

    menu_frame = ctk.CTkFrame(Start_window, height=100)
    menu_frame.pack(pady=5, fill="y", side="top", padx=10)

    # Back button
    button1 = ctk.CTkButton(menu_frame, text="ย้อนกลับ", corner_radius=5, width=15)
    button1.pack(side="left", padx=10, pady=10)

    # Settings button
    button2 = ctk.CTkButton(menu_frame, text="ตั้งค่า", corner_radius=5, width=15)
    button2.pack(side="left", padx=10, pady=10)

    # Face Recognition button
    button3 = ctk.CTkButton(
        menu_frame, text="Face Recognition", corner_radius=5, width=20
    )
    button3.pack(side="left", padx=10, pady=10)

    # Detection Mode
    detection_mode = tk.StringVar(value="None")
    modes = ["Face_Recognition", "YOLO", "Both", "None"]

    # Frame for radio buttons
    radio_frame = ctk.CTkFrame(Start_window, corner_radius=10)
    radio_frame.pack(pady=5, padx=10, fill="x")

    # Create Radio Buttons for detection mode
    for mode in modes:
        rb = ctk.CTkRadioButton(
            radio_frame,
            text=mode,
            variable=detection_mode,
            value=mode,
            corner_radius=5,
            width=20,
        )
        rb.pack(pady=5, padx=10, anchor="w")
    Start_window.mainloop()


start()
