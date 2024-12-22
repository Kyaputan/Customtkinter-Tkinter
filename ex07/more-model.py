import customtkinter as ctk
import os
from PIL import Image
import cv2
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from ultralytics import YOLO
from PIL import Image, ImageTk

images_logos = {}
img_path = None
img_display = None
label_show = None
Select_more = None
single_CNN = None

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
    images_logos["dino_logo"] = ctk.CTkImage(
    light_image=Image.open(os.path.join(image_path, "grounding_dino_logo.png")), size=(30, 30)
    )

Select_more = ctk.CTk()




def more_model():

    load_image()
    Select_more.title("ระบบความปลอดภัย")
    Select_more.geometry("400x300")
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

    # Add Buttons
    CNN_button = ctk.CTkButton(
        menu_frame,
        text="ใช้งานโมเดล CNN",
        image=images_logos["camera_logo"],
        corner_radius=10,
        font=("Helvetica", 16),
        border_width=2,
        command=single_CNN_img
    )
    CNN_button.pack(fill="x", padx=20, pady=10)

    Dino_button = ctk.CTkButton(
        menu_frame,
        text="ใช้งานโมเดล Dino",
        image=images_logos["dino_logo"],
        corner_radius=10,
        font=("Helvetica", 16),
        border_width=2
    )
    Dino_button.pack(fill="x", padx=20, pady=10)

    address_button = ctk.CTkButton(
        menu_frame,
        text="ใช้งานโมเดล ---",
        image=images_logos["IP_address_logo"],
        corner_radius=10,
        font=("Helvetica", 16),
        border_width=2
    )
    address_button.pack(fill="x", padx=20, pady=10)
    
    Select_more.mainloop()

def single_CNN_img():
    global label_show
    single_CNN = ctk.CTkToplevel(Select_more)
    single_CNN.title("face_recording")
    single_CNN.geometry("800x600")
    single_CNN.title("CustomTkinter with YOLO Image Processing")
    single_CNN.resizable(False, False)


    frame_image = ctk.CTkFrame(single_CNN)
    frame_image.pack(pady=20, padx=20, expand=True, fill="both")

    label_show = ctk.CTkLabel(frame_image, text="")
    label_show.pack(expand=True)

    frame_buttons = ctk.CTkFrame(single_CNN)
    frame_buttons.pack(pady=10)

    # ปุ่มเลือกไฟล์
    button1 = ctk.CTkButton(frame_buttons, text="เลือกรูปภาพ", command=select_file)
    button1.pack(side="left", padx=10)

    # ปุ่มประมวลผลด้วย YOLO
    button2 = ctk.CTkButton(frame_buttons, text="ประมวลผล YOLO", command=process_yolo)
    button2.pack(side="right", padx=10)

def load_image_show(filepath):
    global img_display, img_path, label_show
    if label_show is None:
        showinfo(title="Error", message="Label not initialized!")
        return
    
    img = cv2.imread(filepath)
    if img is not None:
        small_frame = cv2.resize(img, (640, 640))
        img = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        img_display = Image.fromarray(img)
        img_display = ImageTk.PhotoImage(img_display)
        label_show.configure(image=img_display)
        label_show.image = img_display  # เก็บ reference เพื่อป้องกันการถูกลบโดย GC
        img_path = filepath
    else:
        showinfo(title="Error", message="Could not load image")


def select_file():
    filetypes = (('Image files', '*.jpg;*.jpeg;*.png'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open an image file', initialdir='/', filetypes=filetypes)
    
    if filename:  
        load_image_show(filename)

def detect_yolo(frame):
    try:
        model = YOLO("CodeCit\Lab4-Customtkinter-Tkinter\ex07\modelYolo.onnx")
        results = model.predict(frame, conf=0.2)
        if len(results[0].boxes) > 0:  # ตรวจสอบว่ามีกล่องตรวจจับ
            return results[0].plot()  # สร้างภาพพร้อมผลการตรวจจับ
        else:
            print("No objects detected")
            return None
    except Exception as e:
        print(f"Error in YOLO detection: {e}")
        return None



def process_yolo():
    global label_show, img_path
    if img_path:
        img = cv2.imread(img_path)  # อ่านภาพจากเส้นทาง
        if img is not None:
            img_yolo = detect_yolo(img)  # ส่งภาพไปที่ YOLO

            if img_yolo is not None:
                img_yolo = cv2.resize(img_yolo, (640, 640))
                img_yolo = cv2.cvtColor(img_yolo, cv2.COLOR_BGR2RGB)
                img_yolo = Image.fromarray(img_yolo)
                img_yolo = ImageTk.PhotoImage(img_yolo)
                label_show.configure(image=img_yolo)
                label_show.image = img_yolo  # เก็บ reference
            else:
                showinfo(title="Error", message="YOLO did not return an image")
        else:
            showinfo(title="Error", message="Could not read image from path")
    else:
        showinfo(title="Error", message="Please select an image first")


more_model()
