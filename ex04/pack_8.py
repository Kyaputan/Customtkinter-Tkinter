import customtkinter as ctk

root = ctk.CTk()

label1 = ctk.CTkLabel(root, text="Padding inside and outside", fg_color="lightgreen")
label1.pack(padx=20, pady=10, ipadx=15, ipady=5)  # Both external and internal padding

root.mainloop()
