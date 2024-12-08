import tkinter as tk
from PIL import Image, ImageTk
import os


def Main_window():
    # Setup window
    root = tk.Tk()
    root.title("ระบบความปลอดภัย")
    root.geometry("1000x700")
    root.resizable(False, False)

    # Image paths
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
    logo_KMITL_image = Image.open(os.path.join(image_path, "KMITL-Photoroom.png"))
    logo_KMITL_image = logo_KMITL_image.resize((130, 130), resample=Image.BICUBIC)
    logo_KMITL_photo = ImageTk.PhotoImage(logo_KMITL_image)

    logo_RIE_image = Image.open(os.path.join(image_path, "RIE-Photoroom.png"))
    logo_RIE_image = logo_RIE_image.resize((130, 130), resample=Image.BICUBIC)
    logo_RIE_photo = ImageTk.PhotoImage(logo_RIE_image)

    # Main container frame
    main_container = tk.Frame(root)
    main_container.pack(fill="both", expand=True, padx=20, pady=20)

    # Header frame with gradient background
    header_frame = tk.Frame(
        main_container, highlightbackground="#ffffff", highlightthickness=2, height=150
    )
    header_frame.pack(fill="x", pady=(0, 20))
    header_frame.pack_propagate(False)

    # Logo layout
    logo_container = tk.Frame(header_frame)
    logo_container.pack(fill="x", padx=20, pady=10)

    navigation_frame_label_KMITL = tk.Label(
        logo_container,
        image=logo_KMITL_photo,
        bg="#ffffff",
        borderwidth=5,
        relief="solid",
    )
    navigation_frame_label_KMITL.pack(side="left", padx=(0, 20))

    logo_rie_label = tk.Label(
        logo_container,
        image=logo_RIE_photo,
        bg="#ffffff",
        borderwidth=5,
        relief="solid",
    )
    logo_rie_label.pack(side="left", padx=(0, 20))

    text_container = tk.Frame(logo_container)
    text_container.pack(side="left", fill="both", expand=True)

    text_rie_label = tk.Label(
        text_container,
        text="สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง\nวิทยาเขตชุมพรเขตรอุดมศักดิ์",
        font=("TH Sarabun New", 24, "bold"),
        justify="left",
    )
    text_rie_label.pack(anchor="w")

    subtitle_label = tk.Label(
        text_container,
        text="Robotics and Intelligent Electronics Engineering",
        font=("TH Sarabun New", 16),
        justify="left",
    )
    subtitle_label.pack(anchor="w")

    # Menu frame with glass effect
    menu_frame = tk.Frame(
        main_container, highlightbackground="#ffffff", highlightthickness=2
    )
    menu_frame.pack(pady=20, padx=100)

    # Title
    logo_label = tk.Label(
        menu_frame, text="ระบบความปลอดภัย", font=("TH Sarabun New", 25, "bold")
    )
    logo_label.pack(padx=40, pady=30)

    # Buttons
    button_width = 50
    button_font = ("TH Sarabun New", 16, "bold")
    button_padding = 1

    start_button = tk.Button(
        menu_frame,
        text="Start",
        fg="black",
        width=button_width,
        font=button_font,
        padx=button_padding,
        pady=button_padding,
        borderwidth=2,
        relief="raised",
    )
    start_button.pack(pady=10)

    face_rec_button = tk.Button(
        menu_frame,
        text="Face Recognition",
        fg="black",
        width=button_width,
        font=button_font,
        padx=button_padding,
        pady=button_padding,
        borderwidth=2,
        relief="raised",
    )
    face_rec_button.pack(pady=10)

    setting_button = tk.Button(
        menu_frame,
        text="Setting",
        fg="black",
        width=button_width,
        height=1,
        font=button_font,
        padx=button_padding,
        pady=button_padding,
        borderwidth=2,
        relief="raised",
    )
    setting_button.pack(pady=10)

    credit_button = tk.Button(
        menu_frame,
        text="Credit",
        fg="black",
        width=button_width,
        height=1,
        font=button_font,
        padx=button_padding,
        pady=button_padding,
        borderwidth=2,
        relief="raised",
    )
    credit_button.pack(pady=10)

    exit_button = tk.Button(
        menu_frame,
        text="Exit",
        fg="black",
        width=button_width,
        height=1,
        font=button_font,
        padx=button_padding,
        pady=button_padding,
        borderwidth=2,
        relief="raised",
    )
    exit_button.pack(pady=(10, 30))

    root.mainloop()


if __name__ == "__main__":
    Main_window()
