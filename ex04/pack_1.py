import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Basic pack() in CustomTkinter")

label1 = ctk.CTkLabel(root, text="CTkLabel 1", fg_color="lightblue")
label1.pack()  # Default pack behavior

label2 = ctk.CTkLabel(root, text="CTkLabel 2", fg_color="lightgreen")
label2.pack()  # Placed below Label 1

root.mainloop()
