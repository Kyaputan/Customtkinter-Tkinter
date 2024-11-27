import customtkinter as ctk

root = ctk.CTk()

label1 = ctk.CTkLabel(root, text="Fill X", fg_color="orange")
label1.pack(fill="x")  # Expands horizontally

label2 = ctk.CTkLabel(root, text="Fill Y", fg_color="purple")
label2.pack(fill="y", side="left")  # Expands vertically on the left

root.mainloop()
