from ultralytics import YOLO

model_path = "CodeCit/Lab5 Customtkinter&Tkinter/ex06/best.pt"
model = YOLO(model_path)

print("Classes:", model.names)