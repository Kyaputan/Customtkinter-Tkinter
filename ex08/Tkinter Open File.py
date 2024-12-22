import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from customtkinter import  CTk, CTkButton 
from PIL import Image, ImageTk
import cv2

def select_file():
    filetypes = (('text files', '*.txt'),('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=filetypes)
    showinfo(title='Selected File',message=filename)
    print(filename)
    
    
root = CTk()
root.title('Tkinter Open File Dialog')
root.resizable(False, False)
root.geometry('300x150')

open_button = CTkButton(root,text='Open a File',command=select_file)

open_button.pack(expand=True)


# run the application
root.mainloop()