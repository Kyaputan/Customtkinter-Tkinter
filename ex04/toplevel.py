import customtkinter as ctk
import tkinter as tk

# Function to update content inside the Toplevel window
def update_toplevel_content(content_type):
    global toplevel_window, content_label  # Use global variables for the Toplevel and content area

    # Clear existing content in the Toplevel
    for widget in toplevel_window.winfo_children():
        widget.destroy()

    # Update content based on the selected type
    if content_type == "Yolo":
        content_label = tk.Label(toplevel_window, text="YOLO Model Selected", font=("Helvetica", 16))
    elif content_type == "Dino":
        content_label = tk.Label(toplevel_window, text="DINO Model Selected", font=("Helvetica", 16))
    elif content_type == "CNN":
        content_label = tk.Label(toplevel_window, text="CNN Model Selected", font=("Helvetica", 16))

    # Place updated content
    content_label.pack(padx=20, pady=20)

# Function to initialize Toplevel window (only called once)
def initialize_toplevel():
    global toplevel_window  # Declare the Toplevel window globally

    # Create Toplevel if not already existing
    toplevel_window = tk.Toplevel()
    toplevel_window.title("Model Viewer")
    toplevel_window.geometry("400x300")

    # Add initial content
    update_toplevel_content("Yolo")  # Default content when opened

# Add Buttons
root = tk.Tk()
root.title("Model Selector")
root.geometry("300x200")

menu_frame = ctk.CTkFrame(root)
menu_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Buttons for each model
Yolo_button = ctk.CTkButton(
    menu_frame,
    text="ใช้งานโมเดล Yolo",
    corner_radius=10,
    font=("Helvetica", 16),
    border_width=2,
    command=lambda: [initialize_toplevel(), update_toplevel_content("Yolo")]
)
Yolo_button.pack(fill="x", padx=20, pady=10)

Dino_button = ctk.CTkButton(
    menu_frame,
    text="ใช้งานโมเดล Dino",
    corner_radius=10,
    font=("Helvetica", 16),
    border_width=2,
    command=lambda: [initialize_toplevel(), update_toplevel_content("Dino")]
)
Dino_button.pack(fill="x", padx=20, pady=10)

CNN_button = ctk.CTkButton(
    menu_frame,
    text="ใช้งานโมเดล CNN",
    corner_radius=10,
    font=("Helvetica", 16),
    border_width=2,
    command=lambda: [initialize_toplevel(), update_toplevel_content("CNN")]
)
CNN_button.pack(fill="x", padx=20, pady=10)

root.mainloop()
