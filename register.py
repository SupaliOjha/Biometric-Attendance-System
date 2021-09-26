from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from mysql.connector import cursor


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1540x800+0+0")

        #=======================variables=======================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_dep=StringVar()
        self.var_sem=StringVar()
        self.var_roll=StringVar()
        self.var_reg=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        #=======bg image============
        img_bg=Image.open(r"C:Images\reg.png")
        img_bg=img_bg.resize((1540,820),Image.ANTIALIAS)
        self.photoimg_bg=ImageTk.PhotoImage(img_bg)

        f_lbl=Label(self.root,image = self.photoimg_bg)
        f_lbl.place(x=0, y=0, width=1540, height=820)

        #=======left image============
        img_left=Image.open(r"C:Images\jis1.jpg")
        img_left=img_left.resize((1540,820),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        left_lbl=Label(self.root,image = self.photoimg_left)
        left_lbl.place(x=130,y=120,width=620,height=580)

        #=========main frame========
        frame=Frame(self.root,bg="white")
        frame.place(x=740,y=120,width=670,height=580)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="navy blue",bg="white")
        register_lbl.place(x=48,y=20)

        #===============label and entry==================

        #-----------row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=70)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15))
        self.fname_entry.place(x=50,y=100,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),fg="black",bg="white")
        l_name.place(x=370,y=70)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=100,width=250)

        #-----------row2

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),fg="black",bg="white")
        contact.place(x=50,y=140)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=170,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=140)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=170,width=250)

        #-----------row3

        security_Q=Label(frame,text="Department",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_Q.place(x=50,y=210)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","BBA","BCA","BME","CE","CSE","ECE","EE","IT","ME","MBA","MCA")
        self.combo_security_Q.place(x=50,y=240,width=250)
        self.combo_security_Q.current(0)

        security_Q=Label(frame,text="Semester",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_Q.place(x=370,y=210)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_sem,font=("times new roman",12,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        self.combo_security_Q.place(x=370,y=240,width=250)
        self.combo_security_Q.current(0)

        #-----------row4

        contact=Label(frame,text="Roll No",font=("times new roman",15,"bold"),fg="black",bg="white")
        contact.place(x=50,y=280)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_roll,font=("times new roman",15))
        self.txt_contact.place(x=50,y=310,width=250)

        email=Label(frame,text="Registration No",font=("times new roman",15,"bold"),fg="black",bg="white")
        email.place(x=370,y=280)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_reg,font=("times new roman",15))
        self.txt_email.place(x=370,y=310,width=250)

        #-----------row5

        security_Q=Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_Q.place(x=50,y=350)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",12,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Nick name","Your Pet Name")
        self.combo_security_Q.place(x=50,y=380,width=250)
        self.combo_security_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),fg="black",bg="white")
        security_A.place(x=370,y=350)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("time new roman",15))
        self.txt_security.place(x=370,y=380,width=250)

        #-----------row6

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        pswd.place(x=50,y=410)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15))
        self.txt_pswd.place(x=50,y=440,width=250)

        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        confirm_pswd.place(x=370,y=410)

        self.txt_confirm=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15))
        self.txt_confirm.place(x=370,y=440,width=250)

        #================Checkbutton====================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms & Conditions",font=("times new roman",12,"bold"),fg="black",bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=480)

        #==================buttons===================
        img=Image.open("Images/register-button-png-18477.png")
        img=img.resize((150,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",fg="black",bg="white")
        b1.place(x=20,y=510,width=200)


        img1=Image.open("Images/login-now-new-md.png")
        img1=img1.resize((150,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,borderwidth=0,cursor="hand2",fg="black",bg="white")
        b1.place(x=345,y=510,width=200)


    #=======================Function Declaration===========================

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_pass.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error!","All fields are required.",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error!","Password & Confirm Password must be same.",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error!","Please agree our terms and conditions.",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Supali@12",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Email alreday Exist",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_dep.get(),
                                                                                        self.var_sem.get(),
                                                                                        self.var_roll.get(),
                                                                                        self.var_reg.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Sucessfully.",parent=self.root)







if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()