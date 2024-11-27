import customtkinter as ctk

ctk.set_appearance_mode("light")

root = ctk.CTk()

label1 = ctk.CTkLabel(root, text="Top", fg_color="lightgrey")
label1.pack(side="top")

label2 = ctk.CTkLabel(root, text="Bottom", fg_color="lightcoral")
label2.pack(side="bottom")

label3 = ctk.CTkLabel(root, text="Left", fg_color="lightblue")
label3.pack(side="left")

label4 = ctk.CTkLabel(root, text="Right", fg_color="lightgreen")
label4.pack(side="right")

root.mainloop()
