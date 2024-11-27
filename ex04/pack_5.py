import customtkinter as ctk

root = ctk.CTk()

label1 = ctk.CTkLabel(root, text="Padding around", fg_color="lightyellow")
label1.pack(padx=20, pady=10)  # Adds external padding

root.mainloop()
