import customtkinter as ctk

root = ctk.CTk()

label1 = ctk.CTkLabel(root, text="Top-Left", fg_color="lightgrey")
label1.pack(anchor="nw")  # Anchored to the top-left corner

label2 = ctk.CTkLabel(root, text="Bottom-Right", fg_color="lightcoral")
label2.pack(anchor="se")  # Anchored to the bottom-right corner

root.mainloop()
