import customtkinter as ctk

# สร้างหน้าต่างหลัก
root = ctk.CTk()

# ตั้งค่าขนาดหน้าต่าง
root.geometry("400x400")

# ตั้งค่าให้แถว 0 และคอลัมน์ 0 สามารถขยายได้
root.grid_rowconfigure(10, weight=1)
root.grid_columnconfigure(10, weight=1)

# สร้างปุ่มใน customtkinter
button1 = ctk.CTkButton(root, text="Button 1")
button2 = ctk.CTkButton(root, text="Button 2")

# จัดปุ่มในกริด
button1.grid(row=0, column=0, sticky="ns")
button2.grid(row=5, column=5, sticky="ns")

root.mainloop()
