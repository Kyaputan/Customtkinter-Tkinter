import customtkinter as ctk

root = ctk.CTk()

frame = ctk.CTkFrame(root, fg_color="lightgrey", width=200, height=100)
frame.pack()

label1 = ctk.CTkLabel(root, text="Outside Frame", fg_color="lightgreen")
label1.pack()

label2 = ctk.CTkLabel(root, text="Inside Frame", fg_color="lightcoral")
label2.pack(in_=frame)  # This label is packed inside the frame

root.mainloop()
