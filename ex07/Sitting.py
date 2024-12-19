import os
import customtkinter as ctk
from PIL import Image
from tkinter import messagebox

# Declare global variables for frames
# url = "" แก้เป็น url_1
ip_camera_url_1 = ""
All_name = ["captain","tee","point"] 
# New
ip_camera_url_1 = ""
ip_camera_url_2 = ""
ip_camera_url_3 = ""
ip_camera_url_4 = ""
ip_camera_url_5 = ""
ip_camera_url_6 = ""

url_1 =""
url_2 =""
url_3 =""
url_4 =""
url_5 =""
url_6 =""

home_frame = None
second_frame = None
Third_frame = None
entry_name = ""
entry_password = ""
url_now = ""
global_selected_quality = ""
images_logos ={}

def quality_selected(selected_port):
    global global_selected_quality
    global_selected_quality = selected_port
    # ตรวจสอบค่าที่เลือก
    if selected_port == "เลือกคุณภาพ":
        print("Selected quality: ไม่มีคุณภาพที่เลือก")
        global_selected_quality = "stream2"
    elif selected_port == "คุณภาพสูง":
        print("Selected quality: stream1")
        global_selected_quality = "stream1"  # อัปเดตค่า
    elif selected_port == "ประสิทธิภาพสูง":
        print("Selected quality: stream2")
        global_selected_quality = "stream2"  # อัปเดตค่า

def input_dialog_Address_1():
    global ip_camera_url_1
    dialog = ctk.CTkInputDialog(text="Type in a number of IP Address \n example : 192.168.0.102" , title="Address")
    address_1 = dialog.get_input()
    if address_1:
        ip_camera_url_1 = address_1
        print("Address :", ip_camera_url_1)
    else:
        print("No address input received")

def input_dialog_Address_2():
    global ip_camera_url_2
    dialog = ctk.CTkInputDialog(text="Type in a number of IP Address \n example : 192.168.0.102" , title="Address")
    address_2 = dialog.get_input()
    if address_2:
        ip_camera_url_2 = address_2
        print("Address :", ip_camera_url_2)
    else:
        print("No address input received")

def input_dialog_Address_3():
    global ip_camera_url_3
    dialog = ctk.CTkInputDialog(text="Type in a number of IP Address \n example : 192.168.0.102" , title="Address")
    address_3 = dialog.get_input()
    if address_3:
        ip_camera_url_3 = address_3
        print("Address :", ip_camera_url_3)
    else:
        print("No address input received")

def input_dialog_Address_4():
    global ip_camera_url_4
    dialog = ctk.CTkInputDialog(text="Type in a number of IP Address \n example : 192.168.0.102" , title="Address")
    address_4 = dialog.get_input()
    if address_4:
        ip_camera_url_4 = address_4
        print("Address :", ip_camera_url_4)
    else:
        print("No address input received")

def input_dialog_Address_5():
    global ip_camera_url_5
    dialog = ctk.CTkInputDialog(text="Type in a number of IP Address \n example : 192.168.0.102" , title="Address")
    address_5 = dialog.get_input()
    if address_5:
        ip_camera_url_5 = address_5
        print("Address :", ip_camera_url_5)
    else:
        print("No address input received")

def input_dialog_Address_6():
    global ip_camera_url_6
    dialog = ctk.CTkInputDialog(text="Type in a number of IP Address \n example : 192.168.0.102" , title="Address")
    address_6 = dialog.get_input()
    if address_6:
        ip_camera_url_6 = address_6
        print("Address :", ip_camera_url_6)
    else:
        print("No address input received")

# def get_credentials(entry_name, entry_password):
#     name = entry_name.get()
#     password = entry_password.get()
#     return name, password

def combine_button_1():
    global url_1, entry_name, entry_password, global_selected_quality, url_now 
    if ip_camera_url_1 and entry_name and entry_password:
        if not global_selected_quality:
            global_selected_quality = "stream2"
        name = entry_name.get()  
        password = entry_password.get() 
        url_1 = f'rtsp://{name}:{password}@{ip_camera_url_1}:554/{global_selected_quality}'
        print("Address:", url_1)
        
        # อัปเดตข้อความใน url_now เพื่อแสดง URL
        url_now.configure(text=f"Link RTSP ของคุณคือ \n {url_1}")
    else:
        print("No address input received")
        messagebox.showerror("Error", "No address input received")

def combine_button_2():
    global url_2, entry_name, entry_password, global_selected_quality, url_now 
    if ip_camera_url_2 and entry_name and entry_password:
        if not global_selected_quality:
            global_selected_quality = "stream2"
        name = entry_name.get()  
        password = entry_password.get() 
        url_2 = f'rtsp://{name}:{password}@{ip_camera_url_2}:554/{global_selected_quality}'
        print("Address:", url_2)
        
        # อัปเดตข้อความใน url_now เพื่อแสดง URL
        url_now.configure(text=f"Link RTSP ของคุณคือ \n {url_2}")
    else:
        print("No address input received")
        messagebox.showerror("Error", "No address input received")

def combine_button_3():
    global url_3, entry_name, entry_password, global_selected_quality, url_now 
    if ip_camera_url_3 and entry_name and entry_password:
        if not global_selected_quality:
            global_selected_quality = "stream2"
        name = entry_name.get()  
        password = entry_password.get() 
        url_3 = f'rtsp://{name}:{password}@{ip_camera_url_3}:554/{global_selected_quality}'
        print("Address:", url_3)
        
        # อัปเดตข้อความใน url_now เพื่อแสดง URL
        url_now.configure(text=f"Link RTSP ของคุณคือ \n {url_3}")
    else:
        print("No address input received")
        messagebox.showerror("Error", "No address input received")

def combine_button_4():
    global url_4, entry_name, entry_password, global_selected_quality, url_now 
    if ip_camera_url_4 and entry_name and entry_password:
        if not global_selected_quality:
            global_selected_quality = "stream2"
        name = entry_name.get()  
        password = entry_password.get() 
        url_4 = f'rtsp://{name}:{password}@{ip_camera_url_4}:554/{global_selected_quality}'
        print("Address:", url_4)
        
        # อัปเดตข้อความใน url_now เพื่อแสดง URL
        url_now.configure(text=f"Link RTSP ของคุณคือ \n {url_4}")
    else:
        print("No address input received")
        messagebox.showerror("Error", "No address input received")

def combine_button_5():
    global url_5, entry_name, entry_password, global_selected_quality, url_now 
    if ip_camera_url_5 and entry_name and entry_password:
        if not global_selected_quality:
            global_selected_quality = "stream2"
        name = entry_name.get()  
        password = entry_password.get() 
        url_5 = f'rtsp://{name}:{password}@{ip_camera_url_5}:554/{global_selected_quality}'
        print("Address:", url_5)
        
        # อัปเดตข้อความใน url_now เพื่อแสดง URL
        url_now.configure(text=f"Link RTSP ของคุณคือ \n {url_5}")
    else:
        print("No address input received")
        messagebox.showerror("Error", "No address input received")

def combine_button_6():
    global url_6, entry_name, entry_password, global_selected_quality, url_now 
    if ip_camera_url_6 and entry_name and entry_password:
        if not global_selected_quality:
            global_selected_quality = "stream2"
        name = entry_name.get()  
        password = entry_password.get() 
        url_6 = f'rtsp://{name}:{password}@{ip_camera_url_6}:554/{global_selected_quality}'
        print("Address:", url_6)
        
        # อัปเดตข้อความใน url_now เพื่อแสดง URL
        url_now.configure(text=f"Link RTSP ของคุณคือ \n {url_6}")
    else:
        print("No address input received")
        messagebox.showerror("Error", "No address input received")

# def show_address():
#     global url_6 , url_5 , url_4 ,url_3 , url_2 , url_1
#     print(f'url_1 {url_1}')
#     print(f'url_2 {url_2}')
#     print(f'url_3 {url_3}')
#     print(f'url_4 {url_4}')
#     print(f'url_5 {url_5}')
#     print(f'url_6 {url_6}')


def change_appearance_mode_event(new_appearance_mode: str):
    ctk.set_appearance_mode(new_appearance_mode)

def change_scaling_event(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    ctk.set_widget_scaling(new_scaling_float)

def show_frame(frame_name):
    global home_frame, second_frame , Third_frame  # Access global frames
    
    # Hide all frames
    home_frame.pack_forget()
    second_frame.pack_forget()
    Third_frame.pack_forget()

    # Show the requested frame
    if frame_name == "home":
        home_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)
    elif frame_name == "frame_2":
        second_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)
    elif frame_name =="frame_3":
        Third_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

def image_logo():
    global images_logos
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
    images_logos["logo_BG_image"] = ctk.CTkImage(Image.open(os.path.join(image_path, "bg_gradient.jpg")), size=(1080, 500))
    images_logos["small_logo_KMITL_image"] = ctk.CTkImage(Image.open(os.path.join(image_path, "KMITL-Photoroom.png")), size=(76, 76))
    images_logos["logo_KMITL_image"] = ctk.CTkImage(Image.open(os.path.join(image_path, "KMITL-Photoroom.png")), size=(130, 130))
    images_logos["logo_RIE_image"] = ctk.CTkImage(Image.open(os.path.join(image_path, "RIE-Photoroom.png")), size=(26, 26))
    images_logos["address_logo"] = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "address-book for light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "address-book for dark.png")), size=(20, 20))
    images_logos["camera_logo"] = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "camera for light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "camera for dark.png")), size=(20, 20))
    images_logos["home_logo"] = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home for light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "home for dark.png")), size=(20, 20))
    images_logos["lock_logo"] = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "lock for light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "lock for dark.png")), size=(20, 20))
    images_logos["sitting_logo"] = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "settings for light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "settings for dark.png")), size=(20, 20))
    images_logos["trash_logo"] = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "trash for light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "trash for dark.png")), size=(20, 20))
    images_logos["user_logo"] = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "user for light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "user for dark.png")), size=(20, 20))
    images_logos["video_logo"] = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "video-camera-alt for light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "video-camera-alt for dark.png")), size=(20, 20))
    images_logos["mode_event_icon"]= ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "contrast.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "moon-phase.png")), size=(30, 30))
    images_logos["IP_address_logo"]= ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "ip-address for light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "ip-address for dark.png")), size=(20, 20))
    images_logos["rescue_logo"] = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "rescue for light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "rescue for dark.png")), size=(30, 30))
    images_logos["baby_logo"] = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "baby for light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "baby for dark.png")), size=(30, 30))
    images_logos["snake_logo"] = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "snake for light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "snake for dark.png")), size=(30, 30))
    images_logos["bandit_logo"] = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "bandit for light.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "bandit for dark.png")), size=(30, 30))
    images_logos["loupe_logo"]= ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "loupe.png")), size=(30, 30))


def sitting():
    global home_frame, second_frame  , Third_frame ,entry_name , entry_password  , url_now
    ctk.set_appearance_mode("Light")
    root = ctk.CTk()
    root.title("image_example.py")
    root.geometry("700x550")

    # load images with light and dark mode image
    image_logo()
    # create navigation frame
    navigation_frame = ctk.CTkFrame(root, corner_radius=20)
    navigation_frame.pack(side="left", fill="y", padx=10, pady=10)

    # create navigation labels and buttons
    navigation_frame_label = ctk.CTkLabel(navigation_frame, text="  SITTING MENU", image=images_logos["small_logo_KMITL_image"],
                                                    compound="left", font=ctk.CTkFont(size=15, weight="bold"),fg_color="white",text_color="#000000")
    navigation_frame_label.pack(pady=20,ipadx=20,fill="x")

    home_button = ctk.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                         fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                         image=images_logos["home_logo"], anchor="w", command=lambda: show_frame("home"))
    home_button.pack(fill="x", pady=5)

    frame_2_button = ctk.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2",
                                            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                            image=images_logos["address_logo"], anchor="w", command=lambda: show_frame("frame_2"))
    frame_2_button.pack(fill="x", pady=5)

    frame_3_button = ctk.CTkButton(navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3",
                                            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                            image=images_logos["sitting_logo"], anchor="w",command=lambda: show_frame("frame_3"))
    frame_3_button.pack(fill="x", pady=5)

    exit_sitting = ctk.CTkButton(navigation_frame, text="Exit", fg_color="red", hover_color="#FF9999",text_color="black")
    exit_sitting.pack(side="bottom", padx=20, pady=20)




    # Create the home_frame
    home_frame = ctk.CTkFrame(root, corner_radius=0, fg_color="transparent")
    home_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Create the bottom part (center, left-bottom, and right-bottom frames)
    mid_frame = ctk.CTkFrame(home_frame, corner_radius=0, fg_color="transparent")
    mid_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Create center frame (above left and right frames)
    center_frame = ctk.CTkFrame(mid_frame, corner_radius=20, fg_color="gray50", height=50)
    center_frame.pack(fill="both", expand=True, padx=10, pady=(10, 10))

    head_User_manual = ctk.CTkLabel(center_frame, text="คู่มือการใช้งานระบบรักษาความปลอดภัย", font=ctk.CTkFont(size=18,weight="bold"),corner_radius=40)
    head_User_manual.pack(pady=(10, 10))

    User_manual_frame = ctk.CTkScrollableFrame(center_frame, corner_radius=40, fg_color="gray70")
    User_manual_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    User_manual_1 = ctk.CTkLabel(User_manual_frame, text="1.ผู้ใช้งานระบบจำเป็นต้องลงทะเบียนกล้องที่ ", image=images_logos["address_logo"],compound="right",font=ctk.CTkFont(size=14),text_color="black")
    User_manual_1.pack(pady=(10,5))

    User_manual_2 = ctk.CTkLabel(User_manual_frame, text="    • กรอกชื่อผู้ใช้ระบบ ", image=images_logos["user_logo"],compound="right",font=ctk.CTkFont(size=14),text_color="black")
    User_manual_2.pack(pady=(5,5))

    User_manual_3 = ctk.CTkLabel(User_manual_frame, text="    • กรอกรหัสผู้ใช้ระบบ ", image=images_logos["lock_logo"],compound="right",font=ctk.CTkFont(size=14),text_color="black")
    User_manual_3.pack(pady=(5,5))

    User_manual_4 = ctk.CTkLabel(User_manual_frame, text="    • กรอก IP ของกล้องผู้ใช้ ", image=images_logos["IP_address_logo"],compound="right",font=ctk.CTkFont(size=14),text_color="black")
    User_manual_4.pack(pady=(5,5))

    User_manual_5 = ctk.CTkLabel(User_manual_frame, text="    • เลือกคุณภาพของภาพ ", image=images_logos["sitting_logo"],compound="right",font=ctk.CTkFont(size=14),text_color="black")
    User_manual_5.pack(pady=(5,5))

    User_manual_6 = ctk.CTkLabel(User_manual_frame, text="2. ระบบสามารถตรวจจับได้ทั้งหมด 4 อย่างได้แก่",font=ctk.CTkFont(size=14),text_color="black")
    User_manual_6.pack(pady=(10,5))

    User_manual_7 = ctk.CTkLabel(User_manual_frame, text="    • คนล้ม  ", image=images_logos["rescue_logo"],compound="right",font=ctk.CTkFont(size=14),text_color="black",anchor="w")
    User_manual_7.pack(pady=(5,5))

    User_manual_8 = ctk.CTkLabel(User_manual_frame, text="    • งู  ", image=images_logos["snake_logo"],compound="right",font=ctk.CTkFont(size=14),text_color="black",anchor="w")
    User_manual_8.pack(pady=(5,5))

    User_manual_9 = ctk.CTkLabel(User_manual_frame, text="    • เด็กสำลอก  ", image=images_logos["baby_logo"],compound="right",font=ctk.CTkFont(size=14),text_color="black",anchor="w")
    User_manual_9.pack(pady=(5,5))

    User_manual_10 = ctk.CTkLabel(User_manual_frame, text="    • คนแปลกหน้า  ", image=images_logos["bandit_logo"],compound="right",font=ctk.CTkFont(size=14),text_color="black",anchor="w")
    User_manual_10.pack(pady=(5,10))


    # Create left-bottom frame (same width as right-frame)
    left_frame = ctk.CTkFrame(mid_frame, corner_radius=30, fg_color=("gray70", "gray30"), height=150,width=100)
    left_frame.pack(side="left", fill="both", expand=True, padx=5, pady=10)

    mode_event = ctk.CTkLabel(left_frame, text="",image=images_logos["mode_event_icon"],width=100, font=ctk.CTkFont(size=14))
    mode_event.pack(pady=(5, 10))

    appearance_mode_menu = ctk.CTkOptionMenu(left_frame, values=["Light", "Dark", "System"], command=change_appearance_mode_event,width=100)
    appearance_mode_menu.pack(pady=(5, 10))  # Span over 3 columns
    appearance_mode_menu.set("Light")
    # Set scaling option menu

    # Create right-bottom frame (same width as left-frame)
    right_frame = ctk.CTkFrame(mid_frame, corner_radius=30, fg_color=("gray70", "gray30"), height=150,width=100)
    right_frame.pack(side="right", fill="both", expand=True, padx=5, pady=10)

    loupe_event = ctk.CTkLabel(right_frame, text="",image=images_logos["loupe_logo"],width=100, font=ctk.CTkFont(size=14))
    loupe_event.pack(pady=(5, 10))

    scaling_optionemenu = ctk.CTkOptionMenu(right_frame, values=["80%", "90%", "100%"], command=change_scaling_event,width=100)
    scaling_optionemenu.pack(pady=(10, 10))  
    scaling_optionemenu.set("100%")

    second_frame = ctk.CTkFrame(root, corner_radius=0, fg_color="transparent")
    second_frame.pack(fill="both", expand=True)
    
    tabview = ctk.CTkTabview(second_frame,corner_radius=5)
    tabview.pack(padx=(5, 5), pady=(10, 10))
    tabview.add("Camera 1")
    tabview.add("Camera 2")
    tabview.add("Camera 3")
    tabview.add("Camera 4")
    tabview.add("Camera 5")
    tabview.add("Camera 6")


    label_Head = ctk.CTkLabel(tabview.tab("Camera 1"), text="ลงข้อมูลเชื่อมต่อระบบ", font=ctk.CTkFont(size=24, weight="bold"))
    label_Head.pack(padx=10, pady=5)
    label_Head = ctk.CTkLabel(tabview.tab("Camera 2"), text="ลงข้อมูลเชื่อมต่อระบบ", font=ctk.CTkFont(size=24, weight="bold"))
    label_Head.pack(padx=10, pady=5)
    label_Head = ctk.CTkLabel(tabview.tab("Camera 3"), text="ลงข้อมูลเชื่อมต่อระบบ", font=ctk.CTkFont(size=24, weight="bold"))
    label_Head.pack(padx=10, pady=5)
    label_Head = ctk.CTkLabel(tabview.tab("Camera 4"), text="ลงข้อมูลเชื่อมต่อระบบ", font=ctk.CTkFont(size=24, weight="bold"))
    label_Head.pack(padx=10, pady=5)
    label_Head = ctk.CTkLabel(tabview.tab("Camera 5"), text="ลงข้อมูลเชื่อมต่อระบบ", font=ctk.CTkFont(size=24, weight="bold"))
    label_Head.pack(padx=10, pady=5)
    label_Head = ctk.CTkLabel(tabview.tab("Camera 6"), text="ลงข้อมูลเชื่อมต่อระบบ", font=ctk.CTkFont(size=24, weight="bold"))
    label_Head.pack(padx=10, pady=5)

    label_width = 80 

    name_frame = ctk.CTkFrame(tabview.tab("Camera 1"), fg_color="transparent")
    name_frame.pack(padx=10, pady=5, fill="x")

    label_name = ctk.CTkLabel(name_frame, text=" ลงชื่อ", image=images_logos["user_logo"], compound="left", width=label_width, anchor="w", font=ctk.CTkFont(size=14))
    label_name.pack(side="left", padx=10, pady=5)

    entry_name = ctk.CTkEntry(name_frame, placeholder_text="Enter name")
    entry_name.pack(side="left", fill="x", expand=True, padx=10)

    password_frame = ctk.CTkFrame(tabview.tab("Camera 1"), fg_color="transparent")
    password_frame.pack(padx=10, pady=5, fill="x")

    label_password = ctk.CTkLabel(password_frame, text=" รหัสผ่าน", image=images_logos["lock_logo"], compound="left", width=label_width, anchor="w", font=ctk.CTkFont(size=14))
    label_password.pack(side="left", padx=10, pady=5)

    entry_password = ctk.CTkEntry(password_frame, show="*", placeholder_text="Enter password")
    entry_password.pack(side="left", fill="x", expand=True, padx=10)

    # Create frame for "Open Address" button and label
    button_frame = ctk.CTkFrame(tabview.tab("Camera 1"), fg_color="transparent")
    button_frame.pack(padx=10, pady=5, fill="x")

    label_button = ctk.CTkLabel(button_frame, text=" IP", image=images_logos["address_logo"], compound="left", width=label_width, anchor="w", font=ctk.CTkFont(size=14))
    label_button.pack(side="left", padx=10, pady=5)

    string_input_button = ctk.CTkButton(button_frame, text="Open Address",command=input_dialog_Address_1)
    string_input_button.pack(side="left", fill="x", expand=True, padx=10)

    # Create frame for port option menu and label
    port_frame = ctk.CTkFrame(tabview.tab("Camera 1"), fg_color="transparent")
    port_frame.pack(padx=10, pady=5, fill="x")

    label_port = ctk.CTkLabel(port_frame, text=" คุณภาพ", image=images_logos["sitting_logo"], compound="left", width=label_width, anchor="w", font=ctk.CTkFont(size=14))
    label_port.pack(side="left", padx=10, pady=5)

    # Create a second option menu for quality selection
    quality_values = ["เลือกคุณภาพ", "คุณภาพสูง", "ประสิทธิภาพสูง"]
    optionmenu_quality_values = ctk.CTkOptionMenu(port_frame, dynamic_resizing=True, values=quality_values,command=quality_selected)
    optionmenu_quality_values.pack(side="left", fill="x", expand=True, padx=10)

    # Agree button
    agree_button = ctk.CTkButton(tabview.tab("Camera 1"), text="agree", fg_color="green", hover_color="#46b842",command=combine_button_1)
    agree_button.pack(pady=10,fill="x", expand=True,padx=40)


    button_frame = ctk.CTkFrame(tabview.tab("Camera 2"), fg_color="transparent")
    button_frame.pack(padx=10, pady=5, fill="x")

    label_button = ctk.CTkLabel(button_frame, text=" IP", image=images_logos["address_logo"], compound="left", width=label_width, anchor="w", font=ctk.CTkFont(size=14))
    label_button.pack(side="left", padx=10, pady=5)

    string_input_button = ctk.CTkButton(button_frame, text="Open Address",command=input_dialog_Address_2)
    string_input_button.pack(side="left", fill="x", expand=True, padx=10)
    
    agree_button = ctk.CTkButton(tabview.tab("Camera 2"), text="agree", fg_color="green", hover_color="#46b842",command=combine_button_2)
    agree_button.pack(pady=10,fill="x", expand=True,padx=40)


    button_frame = ctk.CTkFrame(tabview.tab("Camera 3"), fg_color="transparent")
    button_frame.pack(padx=10, pady=5, fill="x")

    label_button = ctk.CTkLabel(button_frame, text=" IP", image=images_logos["address_logo"], compound="left", width=label_width, anchor="w", font=ctk.CTkFont(size=14))
    label_button.pack(side="left", padx=10, pady=5)

    string_input_button = ctk.CTkButton(button_frame, text="Open Address",command=input_dialog_Address_3)
    string_input_button.pack(side="left", fill="x", expand=True, padx=10)
    
    agree_button = ctk.CTkButton(tabview.tab("Camera 3"), text="agree", fg_color="green", hover_color="#46b842",command=combine_button_3)
    agree_button.pack(pady=10,fill="x", expand=True,padx=40)



    button_frame = ctk.CTkFrame(tabview.tab("Camera 4"), fg_color="transparent")
    button_frame.pack(padx=10, pady=5, fill="x")

    label_button = ctk.CTkLabel(button_frame, text=" IP", image=images_logos["address_logo"], compound="left", width=label_width, anchor="w", font=ctk.CTkFont(size=14))
    label_button.pack(side="left", padx=10, pady=5)

    string_input_button = ctk.CTkButton(button_frame, text="Open Address",command=input_dialog_Address_4)
    string_input_button.pack(side="left", fill="x", expand=True, padx=10)

    agree_button = ctk.CTkButton(tabview.tab("Camera 4"), text="agree", fg_color="green", hover_color="#46b842",command=combine_button_4)
    agree_button.pack(pady=10,fill="x", expand=True,padx=40)



    button_frame = ctk.CTkFrame(tabview.tab("Camera 5"), fg_color="transparent")
    button_frame.pack(padx=10, pady=5, fill="x")

    label_button = ctk.CTkLabel(button_frame, text=" IP", image=images_logos["address_logo"], compound="left", width=label_width, anchor="w", font=ctk.CTkFont(size=14))
    label_button.pack(side="left", padx=10, pady=5)

    string_input_button = ctk.CTkButton(button_frame, text="Open Address",command=input_dialog_Address_5)
    string_input_button.pack(side="left", fill="x", expand=True, padx=10)
    
    agree_button = ctk.CTkButton(tabview.tab("Camera 5"), text="agree", fg_color="green", hover_color="#46b842",command=combine_button_5)
    agree_button.pack(pady=10,fill="x", expand=True,padx=40)



    button_frame = ctk.CTkFrame(tabview.tab("Camera 6"), fg_color="transparent")
    button_frame.pack(padx=10, pady=5, fill="x")
    
    label_button = ctk.CTkLabel(button_frame, text=" IP", image=images_logos["address_logo"], compound="left", width=label_width, anchor="w", font=ctk.CTkFont(size=14))
    label_button.pack(side="left", padx=10, pady=5)

    string_input_button = ctk.CTkButton(button_frame, text="Open Address",command=input_dialog_Address_6)
    string_input_button.pack(side="left", fill="x", expand=True, padx=10)
    
    agree_button = ctk.CTkButton(tabview.tab("Camera 6"), text="agree", fg_color="green", hover_color="#46b842",command=combine_button_6)
    agree_button.pack(pady=10,fill="x", expand=True,padx=40)

    # show_button = ctk.CTkButton(tabview.tab("Camera 6"), text="agree", fg_color="green", hover_color="#46b842",command=show_address)
    # show_button.pack(pady=10,fill="x", expand=True,padx=40)

    label_port = ctk.CTkLabel(second_frame, text="โดยทั่วไปแล้ว RTSP Link จะมีหน้าตาดังนี้ \n rtsp://Rachata:123456@198.162.0.100:554/stream1 \n โดยที่แยกได้เป็นดังนี้ \n rtsp:// ชื่อผู้ใช้ : รหัสผู้ใช้ @ ip_camera: port(554) / คุณภาพ" , font=ctk.CTkFont(size=14))
    label_port.pack( padx=10, pady=5)

    url_now = ctk.CTkLabel(second_frame, text=f" Link RTSP ของคุณคือ \n {url_1}" , font=ctk.CTkFont(size=14))
    url_now.pack( padx=10, pady=5)

    Third_frame = ctk.CTkFrame(root, corner_radius=0, fg_color="transparent")

    main_frame_Third = ctk.CTkFrame(Third_frame, corner_radius=30 ,fg_color="gray")
    main_frame_Third.pack(pady=20,padx=10,fill="both",expand=True)

    Delete_Image_button = ctk.CTkButton(main_frame_Third, text="Delete Image")
    Delete_Image_button.pack(side="bottom",fill="both",pady=(10,20),padx=30, expand=True,anchor="s")

    entry_name_Delete = ctk.CTkEntry(main_frame_Third, placeholder_text="Enter Name")
    entry_name_Delete.pack(side="bottom", fill="x",expand=True, padx=30,anchor="s",pady=(10,0))

    lable_ScrollableFrame =ctk.CTkLabel(main_frame_Third, text="รายชื่อบุคคลที่ลงทะเบียน" , font=ctk.CTkFont(size=25,weight="bold"))
    lable_ScrollableFrame.pack( padx=10, pady=5)

    mane_frame_Third = ctk.CTkScrollableFrame(main_frame_Third, corner_radius=30 ,fg_color="gray70")
    mane_frame_Third.pack(pady=10,padx=20,fill="both",expand=True)

    for name in range(len(All_name)):
        Name = ctk.CTkLabel(mane_frame_Third, text=f"บุคคลที่{name+1} : {All_name[name]}",font=ctk.CTkFont(size=12, weight="normal"))
        Name.pack(padx=10, pady=5)


    show_frame("home")

    root.mainloop()
        
sitting()

