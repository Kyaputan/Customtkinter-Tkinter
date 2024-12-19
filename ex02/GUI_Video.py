import tkinter as tk
from tkinter import Label
import cv2
from PIL import Image, ImageTk
from tkinter import messagebox

# Function to handle the exit button click
def on_exit():
    root.quit()

# Function to update the frame from the camera
def update_frame():
    ret, frame = cap.read()
    if ret:
        # Convert the color from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convert the frame to a PIL Image
        img = Image.fromarray(frame)
        # Convert the PIL Image to an ImageTk
        imgtk = ImageTk.PhotoImage(image=img)
        # Update the Label to show the new frame
        lbl_video.imgtk = imgtk
        lbl_video.config(image=imgtk)
    # Call this function again after 100 milliseconds
    lbl_video.after(100, update_frame)

# Create the main window
root = tk.Tk()
root.title("Live Video in Tkinter")

# Create a Label to display the video
lbl_video = Label(root)
lbl_video.pack()

# Start capturing video from the camera (index 0 means the primary camera)
cap = cv2.VideoCapture(0)

# Create an Exit button
exit_button = tk.Button(root, text="Exit", command=on_exit)
exit_button.pack(pady=10)

# Call the update_frame function for the first time
update_frame()

# Start the application
root.mainloop()

# Release the camera when the window is closed
cap.release()
cv2.destroyAllWindows()
