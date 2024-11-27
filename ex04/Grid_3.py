import customtkinter as ctk
root = ctk.CTk()

# Set grid layout 2x2
root.grid_columnconfigure(1, weight=1)

button1 = ctk.CTkButton(root, text="Button 1")
button2 = ctk.CTkButton(root, text="Button 2")
button3 = ctk.CTkButton(root, text="Button 3")
button4 = ctk.CTkButton(root, text="Button 4")

button1.grid(row=0, column=0)
button2.grid(row=0, column=1, sticky="nsew")
button3.grid(row=1, column=0)
button4.grid(row=1, column=1, sticky="nsew")

root.mainloop()
