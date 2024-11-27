import customtkinter as ctk

# สร้างหน้าต่างหลัก
root = ctk.CTk()

# ตั้งค่าขนาดหน้าต่าง
root.geometry("400x400")

# ตั้งค่าให้ทุกแถวและทุกคอลัมน์สามารถขยายได้
for i in range(2):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# สร้างปุ่มใน customtkinter
button1 = ctk.CTkButton(root, text="Button 1")
button2 = ctk.CTkButton(root, text="Button 2")
button3 = ctk.CTkButton(root, text="Button 3")
button4 = ctk.CTkButton(root, text="Button 4")

# จัดปุ่มในกริด
button1.grid(row=0, column=0, sticky="nsew")
button2.grid(row=0, column=1, sticky="nsew")
button3.grid(row=1, column=0, sticky="nsew")
button4.grid(row=1, column=1, sticky="nsew")

root.mainloop()
