import customtkinter as ctk
import os
from PIL import Image
import tkinter as tk
from tkinter import simpledialog

# Create main window
Additional = ctk.CTk()


def clear_window():
    for widget in Additional.winfo_children():
        widget.destroy()


def Additional_Detection_1():
    clear_window()
    Additional.title("Additional Detection")

    screen_width = Additional.winfo_screenwidth() / 2
    screen_height = Additional.winfo_screenheight() / 2

    # Set window size to full screen
    Additional.geometry(f"{screen_width}x{screen_height}")

    # Get image directory path
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

    # Load images
    logo_KMITL_image = ctk.CTkImage(
        Image.open(os.path.join(image_path, "KMITL-Photoroom.png")), size=(130, 130)
    )
    logo_RIE_image = ctk.CTkImage(
        Image.open(os.path.join(image_path, "RIE-Photoroom.png")), size=(130, 130)
    )

    # Logo frame
    logo_frame = ctk.CTkFrame(Additional)
    logo_frame.pack(fill="x", pady=(0, 10))

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

    text_rie_label = ctk.CTkLabel(
        logo_frame,
        text="สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง วิทยาเขตชุมพรเขตรอุดมศักดิ์\nRobotics and Intelligent Electronics Engineering",
        font=ctk.CTkFont(size=16, weight="bold"),
        justify="left",
    )
    text_rie_label.pack(side="left", padx=10, pady=(10, 10))

    # Video frame container
    video_container = ctk.CTkFrame(Additional)
    video_container.pack(fill="both", expand=True, pady=20)

    # Frame for the video content
    frame_c = ctk.CTkFrame(
        video_container, width=350, height=320, fg_color="white", corner_radius=10
    )
    frame_c.pack(side="top", expand=True, anchor="center", pady=(5, 10), padx=30)

    # Label with an image
    label_c = ctk.CTkLabel(
        frame_c, text="", image=logo_KMITL_image, width=300, height=310
    )
    label_c.pack(side="top", expand=True, pady=(10, 0))

    # Button
    button1 = ctk.CTkButton(frame_c, text="เปิดกล้อง 3")
    button1.pack(side="bottom", pady=(10, 10))

    # Menu frame
    menu_frame = ctk.CTkFrame(Additional, height=100)
    menu_frame.pack(pady=5, fill="y", side="top", padx=10)

    # Add Camera Frames button
    add_camera_button = ctk.CTkButton(
        menu_frame, text="เพิ่มกล้อง", corner_radius=5, width=15, command=add_camera_frames
    )
    add_camera_button.pack(side="left", padx=10, pady=10)

    # Back button
    back_button = ctk.CTkButton(menu_frame, text="ย้อนกลับ", corner_radius=5, width=15)
    back_button.pack(side="left", padx=10, pady=10)


def additional_Detection_2():
    clear_window()
    Additional.title("Main Detection")

    screen_width = Additional.winfo_screenwidth() / 2
    screen_height = Additional.winfo_screenheight() / 2

    # Set window size to full screen
    Additional.geometry(f"{screen_width}x{screen_height}")

    # Get image directory path
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

    # Load images
    logo_KMITL_image = ctk.CTkImage(
        Image.open(os.path.join(image_path, "KMITL-Photoroom.png")), size=(130, 130)
    )
    logo_RIE_image = ctk.CTkImage(
        Image.open(os.path.join(image_path, "RIE-Photoroom.png")), size=(130, 130)
    )

    # Logo frame
    logo_frame = ctk.CTkFrame(Additional)
    logo_frame.pack(fill="x", pady=(0, 10))

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

    text_rie_label = ctk.CTkLabel(
        logo_frame,
        text="สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง วิทยาเขตชุมพรเขตรอุดมศักดิ์\nRobotics and Intelligent Electronics Engineering",
        font=ctk.CTkFont(size=16, weight="bold"),
        justify="left",
    )
    text_rie_label.pack(side="left", padx=10, pady=(10, 10))

    # Video frame container
    video_container = ctk.CTkFrame(Additional)
    video_container.pack(fill="both", expand=True, pady=20)

    # Frame C - Left
    frame_c = ctk.CTkFrame(
        video_container, width=350, height=320, fg_color="white", corner_radius=10
    )
    frame_c.pack(side="left", expand=True, anchor="center", pady=(5, 10), padx=(30, 15))

    label_c = ctk.CTkLabel(
        frame_c, text="", image=logo_KMITL_image, width=300, height=310
    )
    label_c.pack(side="top", expand=True, pady=(10, 0))

    buttonc = ctk.CTkButton(frame_c, text="เปิดกล้อง 3")
    buttonc.pack(side="bottom", pady=(10, 10))

    # Frame D - Right
    frame_d = ctk.CTkFrame(
        video_container, width=350, height=320, fg_color="white", corner_radius=10
    )
    frame_d.pack(side="left", expand=True, anchor="center", pady=(5, 10), padx=(15, 30))

    label_d = ctk.CTkLabel(
        frame_d, text="", image=logo_KMITL_image, width=300, height=310
    )
    label_d.pack(side="top", expand=True, pady=(10, 0))

    buttond = ctk.CTkButton(frame_d, text="เปิดกล้อง 4")
    buttond.pack(side="bottom", pady=(10, 10))

    # Menu frame
    menu_frame = ctk.CTkFrame(Additional, height=100)
    menu_frame.pack(pady=5, fill="y", side="top", padx=10)

    # Add Camera Frames button
    add_camera_button = ctk.CTkButton(
        menu_frame, text="เพิ่มกล้อง", corner_radius=5, width=15, command=add_camera_frames
    )
    add_camera_button.pack(side="left", padx=10, pady=10)

    # Back button
    back_button = ctk.CTkButton(menu_frame, text="ย้อนกลับ", corner_radius=5, width=15)
    back_button.pack(side="left", padx=10, pady=10)


def additional_Detection_3():
    clear_window()
    Additional.title("Main Detection")

    screen_width = Additional.winfo_screenwidth() / 2
    screen_height = Additional.winfo_screenheight() / 2

    # Set window size to full screen
    Additional.geometry(f"{screen_width}x{screen_height}")

    # Get image directory path
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

    # Load images
    logo_KMITL_image = ctk.CTkImage(
        Image.open(os.path.join(image_path, "KMITL-Photoroom.png")), size=(130, 130)
    )
    logo_RIE_image = ctk.CTkImage(
        Image.open(os.path.join(image_path, "RIE-Photoroom.png")), size=(130, 130)
    )

    # Logo frame
    logo_frame = ctk.CTkFrame(Additional)
    logo_frame.pack(fill="x", pady=(0, 10))

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

    text_rie_label = ctk.CTkLabel(
        logo_frame,
        text="สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง วิทยาเขตชุมพรเขตรอุดมศักดิ์\nRobotics and Intelligent Electronics Engineering",
        font=ctk.CTkFont(size=16, weight="bold"),
        justify="left",
    )
    text_rie_label.pack(side="left", padx=10, pady=(10, 10))

    # Video frame container
    video_container = ctk.CTkFrame(Additional)
    video_container.pack(fill="both", expand=True, pady=20)

    # Frame C - Left
    frame_c = ctk.CTkFrame(
        video_container, width=350, height=320, fg_color="white", corner_radius=10
    )
    frame_c.pack(side="left", expand=True, anchor="center", pady=(5, 10), padx=(20, 10))

    label_c = ctk.CTkLabel(
        frame_c, text="", image=logo_KMITL_image, width=300, height=310
    )
    label_c.pack(side="top", expand=True, pady=(10, 0))

    buttonc = ctk.CTkButton(frame_c, text="เปิดกล้อง 3")
    buttonc.pack(side="bottom", pady=(10, 10))

    # Frame D - Center
    frame_d = ctk.CTkFrame(
        video_container, width=350, height=320, fg_color="white", corner_radius=10
    )
    frame_d.pack(side="left", expand=True, anchor="center", pady=(5, 10), padx=(10, 10))

    label_d = ctk.CTkLabel(
        frame_d, text="", image=logo_KMITL_image, width=300, height=310
    )
    label_d.pack(side="top", expand=True, pady=(10, 0))

    buttond = ctk.CTkButton(frame_d, text="เปิดกล้อง 4")
    buttond.pack(side="bottom", pady=(10, 10))

    # Frame E - Right
    frame_e = ctk.CTkFrame(
        video_container, width=350, height=320, fg_color="white", corner_radius=10
    )
    frame_e.pack(side="left", expand=True, anchor="center", pady=(5, 10), padx=(10, 20))

    label_e = ctk.CTkLabel(
        frame_e, text="", image=logo_KMITL_image, width=300, height=310
    )
    label_e.pack(side="top", expand=True, pady=(10, 0))

    buttone = ctk.CTkButton(frame_e, text="เปิดกล้อง 5")
    buttone.pack(side="bottom", pady=(10, 10))

    # Menu frame
    menu_frame = ctk.CTkFrame(Additional, height=100)
    menu_frame.pack(pady=5, fill="y", side="top", padx=10)

    # Add Camera Frames button
    add_camera_button = ctk.CTkButton(
        menu_frame, text="เพิ่มกล้อง", corner_radius=5, width=15, command=add_camera_frames
    )
    add_camera_button.pack(side="left", padx=10, pady=10)

    # Back button
    back_button = ctk.CTkButton(menu_frame, text="ย้อนกลับ", corner_radius=5, width=15)
    back_button.pack(side="left", padx=10, pady=10)


def additional_Detection_4():
    clear_window()
    Additional.title("Main Detection")

    screen_width = Additional.winfo_screenwidth() / 2
    screen_height = Additional.winfo_screenheight() / 2

    # Set window size to full screen
    Additional.geometry(f"{screen_width}x{screen_height}")

    # Get image directory path
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

    # Load images
    logo_KMITL_image = ctk.CTkImage(
        Image.open(os.path.join(image_path, "KMITL-Photoroom.png")), size=(100, 100)
    )
    logo_RIE_image = ctk.CTkImage(
        Image.open(os.path.join(image_path, "RIE-Photoroom.png")), size=(100, 100)
    )

    # Logo frame
    logo_frame = ctk.CTkFrame(Additional)
    logo_frame.pack(fill="x", pady=(0, 10))

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

    text_rie_label = ctk.CTkLabel(
        logo_frame,
        text="สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง วิทยาเขตชุมพรเขตรอุดมศักดิ์\nRobotics and Intelligent Electronics Engineering",
        font=ctk.CTkFont(size=16, weight="bold"),
        justify="left",
    )
    text_rie_label.pack(side="left", padx=10, pady=(10, 10))

    # Video frame container
    video_container = ctk.CTkFrame(Additional)
    video_container.pack(fill="both", expand=True)

    # Top container for 3 frames
    top_container = ctk.CTkFrame(video_container)
    top_container.pack(fill="x", expand=True, pady=(10, 5))

    # Frame C - Top Left
    frame_c = ctk.CTkFrame(
        top_container, width=300, height=200, fg_color="white", corner_radius=10
    )
    frame_c.pack(side="left", expand=True, anchor="center", pady=5, padx=5)

    label_c = ctk.CTkLabel(
        frame_c, text="", image=logo_KMITL_image, width=250, height=190
    )
    label_c.pack(side="top", expand=True, pady=(10, 0))

    buttonc = ctk.CTkButton(frame_c, text="เปิดกล้อง 1")
    buttonc.pack(side="bottom", pady=(10, 10))

    # Frame D - Top Center
    frame_d = ctk.CTkFrame(
        top_container, width=300, height=200, fg_color="white", corner_radius=10
    )
    frame_d.pack(side="left", expand=True, anchor="center", pady=5, padx=5)

    label_d = ctk.CTkLabel(
        frame_d, text="", image=logo_KMITL_image, width=250, height=190
    )
    label_d.pack(side="top", expand=True, pady=(10, 0))

    buttond = ctk.CTkButton(frame_d, text="เปิดกล้อง 2")
    buttond.pack(side="bottom", pady=(10, 10))

    # Bottom container for 2 frames
    bottom_container = ctk.CTkFrame(video_container)
    bottom_container.pack(fill="x", expand=True, pady=(5, 10))

    # Frame E - Top Right
    frame_e = ctk.CTkFrame(
        bottom_container, width=300, height=200, fg_color="white", corner_radius=10
    )
    frame_e.pack(side="left", expand=True, anchor="center", pady=5, padx=5)

    label_e = ctk.CTkLabel(
        frame_e, text="", image=logo_KMITL_image, width=250, height=190
    )
    label_e.pack(side="top", expand=True, pady=(10, 0))

    buttone = ctk.CTkButton(frame_e, text="เปิดกล้อง 3")
    buttone.pack(side="bottom", pady=(10, 10))

    # Frame F - Bottom Left
    frame_f = ctk.CTkFrame(
        bottom_container, width=300, height=200, fg_color="white", corner_radius=10
    )
    frame_f.pack(side="left", expand=True, anchor="center", pady=5, padx=5)

    label_f = ctk.CTkLabel(
        frame_f, text="", image=logo_KMITL_image, width=250, height=190
    )
    label_f.pack(side="top", expand=True, pady=(10, 0))

    buttonf = ctk.CTkButton(frame_f, text="เปิดกล้อง 4")
    buttonf.pack(side="bottom", pady=(10, 10))

    # Menu frame
    menu_frame = ctk.CTkFrame(Additional, height=100)
    menu_frame.pack(pady=5, fill="y", side="top", padx=10)

    # Add Camera Frames button
    add_camera_button = ctk.CTkButton(
        menu_frame, text="เพิ่มกล้อง", corner_radius=5, width=15, command=add_camera_frames
    )
    add_camera_button.pack(side="left", padx=10, pady=10)

    # Back button
    back_button = ctk.CTkButton(menu_frame, text="ย้อนกลับ", corner_radius=5, width=15)
    back_button.pack(side="left", padx=10, pady=10)


def additional_Detection_5():
    clear_window()
    Additional.title("Main Detection")

    screen_width = Additional.winfo_screenwidth() / 2
    screen_height = Additional.winfo_screenheight() / 2

    # Set window size to full screen
    Additional.geometry(f"{screen_width}x{screen_height}")

    # Get image directory path
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")

    # Load images
    logo_KMITL_image = ctk.CTkImage(
        Image.open(os.path.join(image_path, "KMITL-Photoroom.png")), size=(100, 100)
    )
    logo_RIE_image = ctk.CTkImage(
        Image.open(os.path.join(image_path, "RIE-Photoroom.png")), size=(100, 100)
    )

    # Logo frame
    logo_frame = ctk.CTkFrame(Additional)
    logo_frame.pack(fill="x", pady=(0, 10))

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

    text_rie_label = ctk.CTkLabel(
        logo_frame,
        text="สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง วิทยาเขตชุมพรเขตรอุดมศักดิ์\nRobotics and Intelligent Electronics Engineering",
        font=ctk.CTkFont(size=16, weight="bold"),
        justify="left",
    )
    text_rie_label.pack(side="left", padx=10, pady=(10, 10))

    # Video frame container
    video_container = ctk.CTkFrame(Additional)
    video_container.pack(fill="both", expand=True)

    # Top container for 3 frames
    top_container = ctk.CTkFrame(video_container)
    top_container.pack(fill="x", expand=True, pady=(10, 5))

    # Frame C - Top Left
    frame_c = ctk.CTkFrame(
        top_container, width=300, height=200, fg_color="white", corner_radius=10
    )
    frame_c.pack(side="left", expand=True, anchor="center", pady=5, padx=5)

    label_c = ctk.CTkLabel(
        frame_c, text="", image=logo_KMITL_image, width=250, height=190
    )
    label_c.pack(side="top", expand=True, pady=(10, 0))

    buttonc = ctk.CTkButton(frame_c, text="เปิดกล้อง 1")
    buttonc.pack(side="bottom", pady=(10, 10))

    # Frame D - Top Center
    frame_d = ctk.CTkFrame(
        top_container, width=300, height=200, fg_color="white", corner_radius=10
    )
    frame_d.pack(side="left", expand=True, anchor="center", pady=5, padx=5)

    label_d = ctk.CTkLabel(
        frame_d, text="", image=logo_KMITL_image, width=250, height=190
    )
    label_d.pack(side="top", expand=True, pady=(10, 0))

    buttond = ctk.CTkButton(frame_d, text="เปิดกล้อง 2")
    buttond.pack(side="bottom", pady=(10, 10))

    # Frame E - Top Right
    frame_e = ctk.CTkFrame(
        top_container, width=300, height=200, fg_color="white", corner_radius=10
    )
    frame_e.pack(side="left", expand=True, anchor="center", pady=5, padx=5)

    label_e = ctk.CTkLabel(
        frame_e, text="", image=logo_KMITL_image, width=250, height=190
    )
    label_e.pack(side="top", expand=True, pady=(10, 0))

    buttone = ctk.CTkButton(frame_e, text="เปิดกล้อง 3")
    buttone.pack(side="bottom", pady=(10, 10))

    # Bottom container for 2 frames
    bottom_container = ctk.CTkFrame(video_container)
    bottom_container.pack(fill="x", expand=True, pady=(5, 10))

    # Frame F - Bottom Left
    frame_f = ctk.CTkFrame(
        bottom_container, width=300, height=200, fg_color="white", corner_radius=10
    )
    frame_f.pack(side="left", expand=True, anchor="center", pady=5, padx=5)

    label_f = ctk.CTkLabel(
        frame_f, text="", image=logo_KMITL_image, width=250, height=190
    )
    label_f.pack(side="top", expand=True, pady=(10, 0))

    buttonf = ctk.CTkButton(frame_f, text="เปิดกล้อง 4")
    buttonf.pack(side="bottom", pady=(10, 10))

    # Frame G - Bottom Right
    frame_g = ctk.CTkFrame(
        bottom_container, width=300, height=200, fg_color="white", corner_radius=10
    )
    frame_g.pack(side="left", expand=True, anchor="center", pady=5, padx=5)

    label_g = ctk.CTkLabel(
        frame_g, text="", image=logo_KMITL_image, width=250, height=190
    )
    label_g.pack(side="top", expand=True, pady=(10, 0))

    buttong = ctk.CTkButton(frame_g, text="เปิดกล้อง 5")
    buttong.pack(side="bottom", pady=(10, 10))

    # Menu frame
    menu_frame = ctk.CTkFrame(Additional, height=100)
    menu_frame.pack(pady=5, fill="y", side="top", padx=10)

    # Add Camera Frames button
    add_camera_button = ctk.CTkButton(
        menu_frame, text="เพิ่มกล้อง", corner_radius=5, width=15, command=add_camera_frames
    )
    add_camera_button.pack(side="left", padx=10, pady=10)

    # Back button
    back_button = ctk.CTkButton(menu_frame, text="ย้อนกลับ", corner_radius=5, width=15)
    back_button.pack(side="left", padx=10, pady=10)


def add_camera_frames():
    num_frames = simpledialog.askinteger(
        "เพิ่มกล้อง", "ใส่จำนวนกล้อง (1-5):", minvalue=1, maxvalue=5)
    if num_frames == 1:
        Additional_Detection_1()
    elif num_frames == 2:
        additional_Detection_2()
    if num_frames == 3:
        additional_Detection_3()
    elif num_frames == 4:
        additional_Detection_4()
    if num_frames == 5:
        additional_Detection_5()

def start():
    Additional_Detection_1()
    Additional.mainloop()


start()
