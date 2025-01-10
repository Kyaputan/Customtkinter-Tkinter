import customtkinter as ctk
import os
from PIL import Image

images_logos = {}
def load_image():
    global images_logos
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
    images_logos["logo_BG_image"] = ctk.CTkImage(
        Image.open(os.path.join(image_path, "bg_gradient.jpg")), size=(1080, 1080)
    )
    images_logos["small_logo_KMITL_image"] = ctk.CTkImage(
        Image.open(os.path.join(image_path, "KMITL-Photoroom.png")), size=(76, 76)
    )
    images_logos["logo_KMITL_image"] = ctk.CTkImage(
        Image.open(os.path.join(image_path, "KMITL-Photoroom.png")), size=(130, 130)
    )
    images_logos["logo_RIE_image"] = ctk.CTkImage(
        Image.open(os.path.join(image_path, "RIE-Photoroom.png")), size=(130, 130)
    )
    images_logos["small_logo_RIE_image"] = ctk.CTkImage(
    Image.open(os.path.join(image_path, "RIE-Photoroom.png")), size=(76, 76)
    )
    images_logos["address_logo"] = ctk.CTkImage(
        light_image=Image.open(os.path.join(image_path, "address-book for light.png")),
        dark_image=Image.open(os.path.join(image_path, "address-book for dark.png")),
        size=(20, 20),
    )
    images_logos["camera_logo"] = ctk.CTkImage(
        light_image=Image.open(os.path.join(image_path, "camera for light.png")),
        dark_image=Image.open(os.path.join(image_path, "camera for dark.png")),
        size=(20, 20),
    )
    images_logos["home_logo"] = ctk.CTkImage(
        light_image=Image.open(os.path.join(image_path, "home for light.png")),
        dark_image=Image.open(os.path.join(image_path, "home for dark.png")),
        size=(20, 20),
    )
    images_logos["lock_logo"] = ctk.CTkImage(
        light_image=Image.open(os.path.join(image_path, "lock for light.png")),
        dark_image=Image.open(os.path.join(image_path, "lock for dark.png")),
        size=(20, 20),
    )
    images_logos["sitting_logo"] = ctk.CTkImage(
        light_image=Image.open(os.path.join(image_path, "settings for light.png")),
        dark_image=Image.open(os.path.join(image_path, "settings for dark.png")),
        size=(20, 20),
    )
    images_logos["trash_logo"] = ctk.CTkImage(
        light_image=Image.open(os.path.join(image_path, "trash for light.png")),
        dark_image=Image.open(os.path.join(image_path, "trash for dark.png")),
        size=(20, 20),
    )
    images_logos["user_logo"] = ctk.CTkImage(
        light_image=Image.open(os.path.join(image_path, "user for light.png")),
        dark_image=Image.open(os.path.join(image_path, "user for dark.png")),
        size=(20, 20),
    )
    images_logos["video_logo"] = ctk.CTkImage(
        light_image=Image.open(
            os.path.join(image_path, "video-camera-alt for light.png")
        ),
        dark_image=Image.open(
            os.path.join(image_path, "video-camera-alt for dark.png")
        ),
        size=(20, 20),
    )
    images_logos["mode_event_icon"] = ctk.CTkImage(
        light_image=Image.open(os.path.join(image_path, "contrast.png")),
        dark_image=Image.open(os.path.join(image_path, "moon-phase.png")),
        size=(30, 30),
    )
    images_logos["IP_address_logo"] = ctk.CTkImage(
        light_image=Image.open(os.path.join(image_path, "ip-address for light.png")),
        dark_image=Image.open(os.path.join(image_path, "ip-address for dark.png")),
        size=(20, 20),
    )
    images_logos["rescue_logo"] = ctk.CTkImage(
        light_image=Image.open(os.path.join(image_path, "rescue for light.png")),
        dark_image=Image.open(os.path.join(image_path, "rescue for dark.png")),
        size=(30, 30),
    )
    images_logos["baby_logo"] = ctk.CTkImage(
        light_image=Image.open(os.path.join(image_path, "baby for light.png")),
        dark_image=Image.open(os.path.join(image_path, "baby for dark.png")),
        size=(30, 30),
    )
    images_logos["snake_logo"] = ctk.CTkImage(
        light_image=Image.open(os.path.join(image_path, "snake for light.png")),
        dark_image=Image.open(os.path.join(image_path, "snake for dark.png")),
        size=(30, 30),
    )
    images_logos["bandit_logo"] = ctk.CTkImage(
        light_image=Image.open(os.path.join(image_path, "bandit for light.png")),
        dark_image=Image.open(os.path.join(image_path, "bandit for dark.png")),
        size=(30, 30),
    )
    images_logos["loupe_logo"] = ctk.CTkImage(
        light_image=Image.open(os.path.join(image_path, "loupe.png")), size=(30, 30)
    )

def more_model():
    Select_more = ctk.CTk()
    load_image()
    Select_more.title("ระบบความปลอดภัย")
    Select_more.geometry("400x330")
    Select_more.resizable(False, False)
    
    main_container = ctk.CTkFrame(Select_more, fg_color=("#ffffff", "#01061d"),corner_radius=15)
    main_container.pack(fill="both", expand=True, padx= 5, pady=(5,5))


    # Logo layout
    logo_container = ctk.CTkFrame(main_container, fg_color="transparent")
    logo_container.pack(pady=10)

    navigation_frame_label_KMITL = ctk.CTkLabel(
        logo_container,
        text="",
        image=images_logos["small_logo_KMITL_image"],
        fg_color=("#ffffff"),
        corner_radius=15,
    )
    navigation_frame_label_KMITL.pack(side="left", padx=(10, 20))

    logo_rie_label = ctk.CTkLabel(
        logo_container,
        text="",
        image=images_logos["small_logo_RIE_image"],
        fg_color=("#ffffff"),
        corner_radius=15,
    )
    logo_rie_label.pack(side="left", padx=(10, 10))
    
    
    menu_frame = ctk.CTkFrame(
        main_container,
        corner_radius=20,
        fg_color=("#ffffff", "#01061d"),
        border_width=2,
        border_color="#ffffff",
    )
    menu_frame.pack(fill="both",pady=10, padx=10)



    
    
    Select_more.mainloop()


more_model()
