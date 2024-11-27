import customtkinter as ctk

root = ctk.CTk()

label1 = ctk.CTkLabel(root, text="Expand", fg_color="lightpink")
label1.pack(fill="both", expand=True)  # Expands to fill the window

root.mainloop()
