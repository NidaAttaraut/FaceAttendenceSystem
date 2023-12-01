import tkinter as tk
from tkinter import *
import cv2
import numpy as np
import csv
from datetime import datetime
from PIL import ImageTk, Image
import pyttsx3
import face_recognition
import shutil



# Integrated UI
window = Tk()
window.title("Face Recognizer and Attendance System")
window.geometry("1280x720")
window.configure(background="black")

logo = Image.open("unipune.jpg")
logo = logo.resize((1280, 720), Image.ANTIALIAS)  # Resize the image to match the window size
logo1 = ImageTk.PhotoImage(logo)
titl = Label(window, bg="black", relief=RIDGE, bd=10, font=("times new roman", 35))
titl.pack(fill=X)
l1 = Label(window, image=logo1, bg="black",)
l1.place(x=0, y=0)  # Place the image at the top-left corner (0, 0)


from tkinter import *
from PIL import ImageTk, Image


a = tk.Label(
    window,
    text="Face Recognition Attendance System",
    bg="black",
    fg="yellow",
    bd=10,
    font=("times new roman", 35),
)
a.pack()



ri = Image.open("register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=200, y=200)

ai = Image.open("attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=800, y=200)

from enroll_n_save import save_face_encoding
from enroll_n_save import enroll_and_save_name


'''known_face_encodings = []
known_faces_names = []
students = known_faces_names.copy()'''


# Rest of the code for UI creation, buttons, labels, etc.

# Enroll Button (Triggering Function from Prompt 1)
enroll_button = tk.Button(
    window,
    text="Enroll New Person",
    command=enroll_and_save_name,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
enroll_button.place(x=200, y=450)

from attendence import mark_attendance_ui
# Mark Attendance Button (Triggering Function from Prompt 2)
mark_attendance_button = tk.Button(
    window,
    text="Mark Attendance",
    command=mark_attendance_ui,
    bd=10,
    font=("times new roman", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
mark_attendance_button.place(x=800, y=450)

r = tk.Button(
    window,
    text="EXIT",
    bd=10,
    command=quit,
    font=("times new roman", 16),
    bg="black",
    fg="yellow",
    height=2,
    width=17,
)
r.place(x=500, y=550)

# Rest of the code for UI creation, buttons, labels, etc.

window.mainloop()