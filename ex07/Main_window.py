import customtkinter as ctk
import os
from PIL import Image


def Main_window():
    # Setup window
    root = ctk.CTk()
    ctk.set_appearance_mode("dark")
    root.title("ระบบความปลอดภัย")
    root.geometry("1000x700")
    root.resizable(False, False)

    # Image paths
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
    logo_KMITL_image = ctk.CTkImage(
        Image.open(os.path.join(image_path, "KMITL-Photoroom.png")), size=(130, 130)
    )
    logo_RIE_image = ctk.CTkImage(
        Image.open(os.path.join(image_path, "RIE-Photoroom.png")), size=(130, 130)
    )
    logo_BG_image = ctk.CTkImage(
        Image.open(os.path.join(image_path, "bg_gradient.jpg")), size=(1000, 1000)
    )

    # Background
    bg_image_label = ctk.CTkLabel(root, text="", image=logo_BG_image)
    bg_image_label.place(relx=0, rely=0, relwidth=1, relheight=1)
    bg_image_label.lower()

    # Main container frame
    main_container = ctk.CTkFrame(root, fg_color=("#ffffff", "lightgray"))
    main_container.pack(fill="both", expand=True, padx=20, pady=20)

    # Header frame with gradient background
    header_frame = ctk.CTkFrame(
        main_container, corner_radius=15, fg_color=("#ffffff", "lightgray"), height=150
    )
    header_frame.pack(fill="x", pady=(0, 20))
    header_frame.pack_propagate(False)

    # Logo layout
    logo_container = ctk.CTkFrame(header_frame, fg_color="transparent")
    logo_container.pack(fill="x", padx=20, pady=10)

    navigation_frame_label_KMITL = ctk.CTkLabel(
        logo_container,
        text="",
        image=logo_KMITL_image,
        fg_color=("#ffffff", "lightgray"),
        corner_radius=15,
    )
    navigation_frame_label_KMITL.pack(side="left", padx=(0, 20))

    logo_rie_label = ctk.CTkLabel(
        logo_container,
        text="",
        image=logo_RIE_image,
        fg_color=("#ffffff", "lightgray"),
        corner_radius=15,
    )
    logo_rie_label.pack(side="left", padx=(0, 20))

    text_container = ctk.CTkFrame(logo_container, fg_color="transparent")
    text_container.pack(side="left", fill="both", expand=True)

    text_rie_label = ctk.CTkLabel(
        text_container,
        text="สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบังวิทยาเขตชุมพรเขตรอุดมศักดิ์",
        font=ctk.CTkFont(family="FC Minimal", size=21, weight="bold"),
        justify="left",
        text_color="#E35205",
    )
    text_rie_label.pack(anchor="w", pady=(50, 10))

    subtitle_label = ctk.CTkLabel(
        text_container,
        text="Robotics and Intelligent Electronics Engineering",
        font=ctk.CTkFont(family="FC Minimal", size=21, weight="bold"),
        justify="left",
        text_color="#E35205",
    )
    subtitle_label.pack(anchor="w")

    # Menu frame with glass effect
    menu_frame = ctk.CTkFrame(
        main_container,
        corner_radius=20,
        fg_color=("#ffffff", "lightgray"),
        border_width=2,
        border_color="#ffffff",
    )
    menu_frame.pack(pady=20, padx=100)

    # Title
    logo_label = ctk.CTkLabel(
        menu_frame,
        text="ระบบความปลอดภัย",
        font=ctk.CTkFont(family="FC Minimal", size=48, weight="bold"),
        text_color="#E35205",
    )
    logo_label.pack(padx=40, pady=30)

    # Buttons
    button_style = {
        "height": 40,
        "width": 200,
        "corner_radius": 10,
        "font": ctk.CTkFont(family="FC Minimal", size=16, weight="bold"),
        "border_width": 2,
    }

    start_button = ctk.CTkButton(
        menu_frame,
        text="Start",
        fg_color="#E35205",
        hover_color="#45a049",
        border_color="#333333",
        **button_style
    )
    start_button.pack(pady=10)

    face_rec_button = ctk.CTkButton(
        menu_frame,
        text="Face Recognition",
        fg_color="#E35205",
        hover_color="#1976D2",
        border_color="#333333",
        **button_style
    )
    face_rec_button.pack(pady=10)

    setting_button = ctk.CTkButton(
        menu_frame,
        text="Setting",
        fg_color="#E35205",
        hover_color="#FFA000",
        border_color="#333333",
        **button_style
    )
    setting_button.pack(pady=10)

    credit_button = ctk.CTkButton(
        menu_frame,
        text="Credit",
        fg_color="#E35205",
        hover_color="#757575",
        border_color="#333333",
        **button_style
    )
    credit_button.pack(pady=10)

    exit_button = ctk.CTkButton(
        menu_frame,
        text="Exit",
        fg_color="#E35205",
        hover_color="#d32f2f",
        border_color="#333333",
        **button_style
    )
    exit_button.pack(pady=(10, 30))

    root.mainloop()


if __name__ == "__main__":
    Main_window()
