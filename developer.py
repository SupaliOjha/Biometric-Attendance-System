from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Biometric Attendance System")


        #dev img
        title_lbl = Label(self.root, bd=2, bg="dark blue", relief=RIDGE, text="DEVELOPERS", fg="white", font=("times new roman",35,"bold"))
        title_lbl.place (x=0, y=0, width=1540, height=55)

        img_top=Image.open(r"Images\devs.png")
        img_top=img_top.resize((1540,750),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1540, height=750)


        #================time=================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl = Label(title_lbl, font=('times new roman',25,'bold'), bg='dark blue',fg='white')
        lbl.place(x=1320,y=0,width=210,height=50)
        time()

        
        #frame
        main_frame = Frame(f_lbl,bd=2, bg="white")
        main_frame.place (x=13, y=300, width=550, height=470)

        #supali
        img1=Image.open(r"Images\sup.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1_top=ImageTk.PhotoImage(img1)

        f_lbl=Label(main_frame,image = self.photoimg1_top)
        f_lbl.place(x=437, y=10, width=100, height=100)

        sup_frame = Frame(main_frame,bd=2, bg="white")
        sup_frame.place (x=10, y=5, width=415, height=100)

        sup_label=Label(sup_frame,text="Hello Everyone!",font=("Times New Roman",12,"bold"),bg="white", fg="navy blue")
        sup_label.place(x=5, y=5)
        sup_label=Label(sup_frame,text="Myself Supali Ojha.",font=("Times New Roman",12,"bold"),bg="white", fg="navy blue")
        sup_label.place(x=5, y=25)
        sup_label=Label(sup_frame,text="I'm a CSE undergrad student of JIS College Of Engineering.",font=("Times New Roman",12,"bold"),bg="white", fg="navy blue")
        sup_label.place(x=5, y=45)
        sup_label=Label(sup_frame,text="I've a curiosity to explore and learn new things.",font=("Times New Roman",12,"bold"),bg="white", fg="navy blue")
        sup_label.place(x=5, y=67)


        #ankita
        img2=Image.open(r"Images\anki.jpg")
        img2=img2.resize((100,100),Image.ANTIALIAS)
        self.photoimg2_top=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image = self.photoimg2_top)
        f_lbl.place(x=15, y=110, width=100, height=100)

        anki_frame = Frame(main_frame,bd=2, bg="white")
        anki_frame.place (x=115, y=110, width=415, height=100)

        anki_label=Label(anki_frame,text="Hey There!",font=("Times New Roman",12,"bold"),bg="white", fg="magenta")
        anki_label.place(x=5, y=5)
        anki_label=Label(anki_frame,text="My name is Ankita Saha.",font=("Times New Roman",12,"bold"),bg="white", fg="magenta")
        anki_label.place(x=5, y=25)
        anki_label=Label(anki_frame,text="I'm pursuing B.Tech from JIS College Of Engineering.",font=("Times New Roman",12,"bold"),bg="white", fg="magenta")
        anki_label.place(x=5, y=45)
        anki_label=Label(anki_frame,text="I've also done diploma in Computer Science and Engineering.",font=("Times New Roman",12,"bold"),bg="white", fg="magenta")
        anki_label.place(x=5, y=67)

        #aparupa
        img3=Image.open(r"Images\apu.jpg")
        img3=img3.resize((100,100),Image.ANTIALIAS)
        self.photoimg3_top=ImageTk.PhotoImage(img3)

        f_lbl=Label(main_frame,image = self.photoimg3_top)
        f_lbl.place(x=437, y=220, width=100, height=100)

        apu_frame = Frame(main_frame,bd=2, bg="white")
        apu_frame.place (x=10, y=220, width=415, height=100)

        apu_label=Label(apu_frame,text="Hello Everyone!",font=("Times New Roman",12,"bold"),bg="white", fg="navy blue")
        apu_label.place(x=0, y=5)
        apu_label=Label(apu_frame,text="My name is Aparupa Chakraborty.",font=("Times New Roman",12,"bold"),bg="white", fg="navy blue")
        apu_label.place(x=0, y=25)
        apu_label=Label(apu_frame,text="I belongs to Tripura in India.",font=("Times New Roman",12,"bold"),bg="white", fg="navy blue")
        apu_label.place(x=0, y=45)
        apu_label=Label(apu_frame,text="I'm pursuing B.Tech on CSE from JIS College of Engineering.",font=("Times New Roman",12,"bold"),bg="white", fg="navy blue")
        apu_label.place(x=0, y=67)


        #joy
        img4=Image.open(r"Images\joy.jpg")
        img4=img4.resize((100,100),Image.ANTIALIAS)
        self.photoimg4_top=ImageTk.PhotoImage(img4)

        f_lbl=Label(main_frame,image = self.photoimg4_top)
        f_lbl.place(x=15, y=330, width=100, height=100)

        joy_frame = Frame(main_frame,bd=2, bg="white")
        joy_frame.place (x=115, y=330, width=415, height=100)

        joy_label=Label(joy_frame,text="Hey All!",font=("Times New Roman",12,"bold"),bg="white", fg="magenta")
        joy_label.place(x=5, y=5)
        joy_label=Label(joy_frame,text="My name is Joyshankar Mandal.",font=("Times New Roman",12,"bold"),bg="white", fg="magenta")
        joy_label.place(x=5, y=25)
        joy_label=Label(joy_frame,text="I'm pursuing B.Tech from JIS College Of Engineering.",font=("Times New Roman",12,"bold"),bg="white", fg="magenta")
        joy_label.place(x=5, y=45)
        joy_label=Label(joy_frame,text="I've also done diploma in Computer Science and Engineering.",font=("Times New Roman",12,"bold"),bg="white", fg="magenta")
        joy_label.place(x=5, y=67)





if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()