from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from time import strftime
from datetime import datetime
import os
import mysql.connector
from student import Student
from developer import Developer
from chatbot import ChatBot
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Biometric Attendance System")

        
        #1st image
        img1=Image.open(r"C:Images\jis1.jpg")
        img1=img1.resize((520,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image = self.photoimg1)
        f_lbl.place(x=0, y=0, width=520, height=100)


        #2nd image
        img2=Image.open(r"Images\facialrecognition.png")
        img2=img2.resize((520,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image = self.photoimg2)
        f_lbl.place(x=520, y=0, width=520, height=100)


        #3rd image
        img3=Image.open(r"Images\jis1.jpg")
        img3=img3.resize((520,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image = self.photoimg3)
        f_lbl.place(x=1040, y=0, width=520, height=100)


        #bg image
        img4=Image.open(r"Images\jis3.jpg")
        img4=img4.resize((1540,730),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image = self.photoimg4)
        bg_img.place(x=0, y=100, width=1540, height=730)

        title_lbl = Label(bg_img,text="JIS College Of Engineering Biometric Attendance System", font=("Times New Roman",25,"bold"), bg="white", fg="navy blue")
        title_lbl.place(x=0, y=0, width=1540, height=45)


        #================time=================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl = Label(title_lbl, font=('times new roman',20,'bold'), bg='white',fg='navy blue')
        lbl.place(x=1335,y=-5,width=210,height=50)
        time()


        #student button
        img5=Image.open(r"Images\student.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img, image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=150, y=110, width=220, height=220)

        b1_1=Button(bg_img, text="Student Details",command=self.student_details, cursor="hand2", font=("Helvetica",20,"bold"), bg="dark blue", fg="white")
        b1_1.place(x=150, y=310, width=220, height=40)


        #Face Detection button
        img6=Image.open(r"Images\face_detector1.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image = self.photoimg6, cursor="hand2", command=self.face_data)
        b1.place(x=480, y=110, width=220, height=220)

        b1_1=Button(bg_img, text = "Face Detector", cursor="hand2", command=self.face_data, font=("Helvetica",20,"bold"), bg="dark blue", fg="white")
        b1_1.place(x=480, y=310, width=220, height=40)


        #Attendance button
        img7=Image.open(r"Images\attendance1.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image = self.photoimg7, cursor="hand2",command=self.attendance_data)
        b1.place(x=810, y=110, width=220, height=220)

        b1_1=Button(bg_img, text = "Attendance", cursor="hand2",command=self.attendance_data, font=("Helvetica",20,"bold"), bg="dark blue", fg="white")
        b1_1.place(x=810, y=310, width=220, height=40)


        #Train Data button
        img8=Image.open(r"Images\traindata.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image = self.photoimg8, cursor="hand2", command=self.train)
        b1.place(x=1140, y=110, width=220, height=220)

        b1_1=Button(bg_img, text = "Train Data", cursor="hand2",command=self.train, font=("Helvetica",20,"bold"), bg="dark blue", fg="white")
        b1_1.place(x=1140, y=310, width=220, height=40)


        #Gallery button
        img9=Image.open(r"Images\gallery.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image = self.photoimg9, cursor="hand2", command=self.open_img)
        b1.place(x=310, y=410, width=220, height=220)

        b1_1=Button(bg_img, text = "Gallery", cursor="hand2", command=self.open_img, font=("Helvetica",20,"bold"), bg="dark blue", fg="white")
        b1_1.place(x=310, y=610, width=220, height=40)





        #Exit button
        img12=Image.open(r"Images\exit.png")
        img12=img12.resize((220,220),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image = self.photoimg12, command=self.iExit, cursor="hand2")
        b1.place(x=980, y=410, width=220, height=220)

        b1_1=Button(bg_img, text = "Sign Out", cursor="hand2",command=self.iExit, font=("Helvetica",20,"bold"), bg="dark blue", fg="white")
        b1_1.place(x=980, y=610, width=220, height=40)


    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Exit!","Are You Sure?", parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

        #=================Function button====================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    

    def train(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)






if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()