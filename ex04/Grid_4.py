import customtkinter as ctk

# สร้างหน้าต่างหลัก
root = ctk.CTk()
root.geometry("400x400")

# กำหนดแถวและคอลัมน์เพื่อให้ขยายได้
for i in range(7):  # 3 คอลัมน์
    root.grid_columnconfigure(i, weight=1)

for i in range(6):  # 5 แถว (นับรวมแถวที่วางปุ่มขวาบน)
    root.grid_rowconfigure(i, weight=1)

# สร้างปุ่มขวาบน (3 ปุ่มในแถวเดียวกัน)
button1 = ctk.CTkButton(root, text="Button 1")
button2 = ctk.CTkButton(root, text="Button 2")
button3 = ctk.CTkButton(root, text="Button 3")
button_t = ctk.CTkButton(root, text="Button t")

# วางปุ่มในกริดตำแหน่งขวาบน
button1.grid(row=0, column=1)
button2.grid(row=0, column=2)
button3.grid(row=0, column=3)
button_t.grid(row=0, column=5)
# สร้างปุ่มสำหรับตรงกลางจอ (4 ปุ่มในแนวตั้ง)
button4 = ctk.CTkButton(root, text="Button 4")
button5 = ctk.CTkButton(root, text="Button 5")
button6 = ctk.CTkButton(root, text="Button 6")
button7 = ctk.CTkButton(root, text="Button 7")

# วางปุ่มในกริดตำแหน่งตรงกลางจอ (คอลัมน์ 1)
button4.grid(row=2, column=2, sticky="nsew")
button5.grid(row=3, column=2, sticky="nsew")
button6.grid(row=4, column=2, sticky="nsew")
button7.grid(row=5, column=2, sticky="nsew")

root.mainloop()
