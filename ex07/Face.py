import customtkinter as ctk
import os
from PIL import Image
import tkinter as tk
All_name =[]
face_window = ctk.CTk() 

def find_names():
    global All_name
    folder_path = "CodeCit/Lab5 Customtkinter&Tkinter/ex06/Face_reg"
    
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg"):
            name_without_extension = os.path.splitext(filename)[0]  # ตัดส่วนขยายออก
            All_name.append(name_without_extension)  # เก็บเฉพาะชื่อไฟล์
    return All_name

def face_recording():
    global face_window, label_r , entry_name
    find_names()
    face_window.title("face_recording")


    # Set window size to full screen
    face_window.geometry(f"{1080}x{720}")
    face_window.resizable(False, False)
    
    # Get image directory path
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
    
    # Load two images
    logo_KMITL_image = ctk.CTkImage(Image.open(os.path.join(image_path, "KMITL-Photoroom.png")), size=(130, 130))
    logo_RIE_image = ctk.CTkImage(Image.open(os.path.join(image_path, "RIE-Photoroom.png")), size=(130, 130))
    logo_BG_image = ctk.CTkImage(Image.open(os.path.join(image_path, "bg_gradient.jpg")), size=(1080 , 720))

    # Background image
    bg_image_label = ctk.CTkLabel(face_window, text="", image=logo_BG_image)

    bg_image_label.place(relx=0, rely=0, relwidth=1, relheight=1)  # Fill the entire window
    # Lower the background image to be behind other widgets
    bg_image_label.lower()
    # Configure logo frame
    logo_frame = ctk.CTkFrame(face_window)
    logo_frame.pack(fill="x", pady=(0,10))  # Centering the frame horizontally with some padding

    navigation_frame_label_KMITL = ctk.CTkLabel(logo_frame, text="", image=logo_KMITL_image, font=ctk.CTkFont(size=16, weight="bold"),fg_color="white",corner_radius=20)
    navigation_frame_label_KMITL.pack(side="left", padx=20,pady=(10,10))

    logo_rie_label = ctk.CTkLabel(logo_frame, text="", image=logo_RIE_image,fg_color="white",corner_radius=20)
    logo_rie_label.pack(side="left",pady=(10,10))

    # Create the label for the text (separate from the logo)
    text_rie_label = ctk.CTkLabel(logo_frame, text="สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง วิทยาเขตชุมพรเขตรอุดมศักดิ์\nRobotics and Intelligent Electronics Engineering", 
                                font=ctk.CTkFont(size=16, weight="bold"), justify="left")
    text_rie_label.pack(side="left", padx=10,pady=(10,10))

    main_frame = ctk.CTkFrame(face_window,fg_color="black")
    main_frame.pack(fill="y",  pady=20)  # Fill the remaining space

    video_frame = ctk.CTkFrame(main_frame,fg_color="#161616")
    video_frame.pack(side="left",fill="y")

    frame_r = ctk.CTkFrame(video_frame, width=320, height=320, fg_color="white",corner_radius=20) 
    frame_r.pack(expand=True,anchor="n",pady=(5,10),padx=(30,30)) 
    label_r = ctk.CTkLabel(frame_r, text="",image=logo_KMITL_image,width=320, height=320)
    label_r.pack(side="top", expand=True, padx=10,pady=10)  # Expand to fill remaining space
    button1 = ctk.CTkButton(frame_r, text="เปิดกล้อง")
    button1.pack(side="bottom",pady=10)
    exit_bottom = ctk.CTkButton(video_frame, text="Exit", fg_color="red",text_color="black")
    exit_bottom.pack(padx=10,pady=(10,5))

    input_data_frame =ctk.CTkFrame(main_frame)
    input_data_frame.pack(side="right",fill="y", padx=(30,30) , pady=(5,10))

    label_name = ctk.CTkLabel(input_data_frame, text="ใส่ชื่อ",font=ctk.CTkFont(size=16, weight="bold"))
    label_name.pack(padx=10,pady=5)
    entry_name = ctk.CTkEntry(input_data_frame, placeholder_text="Enter image name")
    entry_name.pack(padx=10,pady=5)

    btn_save_b = ctk.CTkButton(input_data_frame, text="Save Image", fg_color="#3fd956",text_color="black")
    btn_save_b.pack(padx=10,pady=(10,5))

    btn_delete_b = ctk.CTkButton(input_data_frame, text="Delete Image",fg_color="red",text_color="black")
    btn_delete_b.pack(padx=10,pady=5)

    scrollable_frame = ctk.CTkScrollableFrame(input_data_frame, label_text="CTkScrollableFrame")
    scrollable_frame.pack(padx=10,pady=5)
    for name in range(len(All_name)):
        Name = ctk.CTkLabel(scrollable_frame, text=f"บุคคลที่{name+1} : {All_name[name]}",font=ctk.CTkFont(size=12, weight="normal"))  # แสดงชื่อจาก All_name
        Name.pack(padx=10, pady=5)

    face_window.mainloop()

face_recording()
