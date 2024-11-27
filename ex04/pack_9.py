import customtkinter as ctk

root = ctk.CTk()

label1 = ctk.CTkLabel(root, text="CTkLabel 1", fg_color="lightblue")
label1.pack()

label2 = ctk.CTkLabel(root, text="CTkLabel 2", fg_color="lightgreen")
label2.pack()

label3 = ctk.CTkLabel(root, text="CTkLabel 3", fg_color="lightpink")
label3.pack(before=label2)  # Places Label 3 before Label 2

root.mainloop()
