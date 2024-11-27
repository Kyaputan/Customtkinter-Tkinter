import customtkinter as ctk

root = ctk.CTk()

label1 = ctk.CTkLabel(root, text="Internal Padding", fg_color="lightblue")
label1.pack(ipadx=20, ipady=10)  # Adds internal padding

root.mainloop()
