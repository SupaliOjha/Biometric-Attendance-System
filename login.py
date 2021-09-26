from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import tkinter
import os
from student import Student
from developer import Developer
from chatbot import ChatBot
from train import Train
from face_recognition import Face_Recognition


def main():
    win=Tk()
    app=Login(win)
    win.mainloop()


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1540x800+0+0")

        img_bg=Image.open(r"C:Images\login1.jpg")
        img_bg=img_bg.resize((1540,820),Image.ANTIALIAS)
        self.photoimg_bg=ImageTk.PhotoImage(img_bg)

        f_lbl=Label(self.root,image = self.photoimg_bg)
        f_lbl.place(x=0, y=0, width=1540, height=820)


        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"Images/users.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="Login To Your Account",font=("times new roman",20,"bold"),fg="navy blue",bg="white")
        get_str.place(x=25,y=100)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",18,"bold"),fg="black",bg="white")
        username.place(x=70,y=160)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15))
        self.txtuser.place(x=35,y=190,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",18,"bold"),fg="black",bg="white")
        password.place(x=70,y=230)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15))
        self.txtpass.place(x=35,y=260,width=270)
        
        #========Icon Image==============
        img2=Image.open(r"Images/user.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="white",borderwidth=0)
        lblimg1.place(x=645,y=334,width=25,height=25)

        img3=Image.open(r"Images/pw.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="white",borderwidth=0)
        lblimg1.place(x=645,y=404,width=25,height=25)

        #loginbutton
        loginbtn=Button(frame,command=self.login, text="Login",font=("times new roman",20,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=305,width=120,height=38)

        # registerbutton
        loginbtn=Button(frame,command=self.register_window,text="New User Register",font=("times new roman",13,"bold"),borderwidth=0,fg="navy blue",bg="white",activeforeground="white",activebackground="white")
        loginbtn.place(x=25,y=365,width=160)

        #forgetpassbtn
        loginbtn=Button(frame,command=self.forgot_password_windo,text="Forget Password?",font=("times new roman",13,"bold"),borderwidth=0,fg="navy blue",bg="white",activeforeground="white",activebackground="white")
        loginbtn.place(x=23,y=390,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Plaese Enter The User ID",parent=self.root)
        if  self.txtpass.get()=="":
            messagebox.showerror("Error","Plaese Enter The Password",parent=self.root)

        if self.txtuser.get()=="admin" and self.txtpass.get()=="admin":
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition_System(self.new_window)
            return
            
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Supali@12",database="face_recognizer")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                            ))

            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid user name & password",parent=self.root)
            else:
                open_main=messagebox.askyesno("YesNo","If You Are Admin, Use Admin ID & Password \n \n Are You Admin?",parent=self.root)
                if open_main>0:
                    if not open_main:
                        return
                else:
                    self.new_window=Toplevel(self.root)
                    self.app=Student(self.new_window)
                    
            conn.commit()
            conn.close()


    #=====================reset password========================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Erro: Empty Question","Please Select The Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error: No Answer","Please Enter Security Answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error: Empty New Password","Please Enter The New Password",parent=self.root2)

        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Supali@12",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error: Wrong Answer","Selected Security Question is Wrong.",parent=self.root2)

            else:
                conn=mysql.connector.connect(host="localhost",user="root",password="Supali@12",database="face_recognizer")
                my_cursor=conn.cursor()
                query=("select * from register where email=%s and securityA=%s")
                value=(self.txtuser.get(),self.txt_security.get())
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error: Wrong Answer","Entered Answer is Wrong.",parent=self.root2)
                else:
                    query=("update register set password=%s where email=%s")
                    value=(self.txt_newpass.get(),self.txtuser.get())
                    my_cursor.execute(query,value)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success","Your Password is Successfully Changed.",parent=self.root2)
                    self.root2.destroy()




    #==================Forget password window=====================
    def forgot_password_windo(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Plaese Enter the Email to reset password",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Supali@12",database="face_recognizer")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Wrong Email","Student Email ID not Found.",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Quetions",font=("times new roman",15,"bold"))
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",12,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Nick name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)




                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"))
                security_A.place(x=59,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("time new roman",12))
                self.txt_security.place(x=50,y=180,width=250)


                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"))
                new_password.place(x=59,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("time new roman",12))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Save Change",command=self.reset_pass,font=("times new roman",15,"bold"),fg="white",bg="red")
                btn.place(x=100,y=290)
                        






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
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",fg="black",bg="white")
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

    def return_login(self):
        self.root.destroy()
        


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Biometric Attendance System")


        #=================Variables====================
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_batch=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_div=StringVar()
        self.var_id=StringVar()
        self.var_reg=StringVar()
        self.var_roll=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_mentor=StringVar()



        #1st image
        img1=Image.open(r"Images\jis1.jpg")
        img1=img1.resize((520,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image = self.photoimg1)
        f_lbl.place(x=0, y=0, width=520, height=100)


        #2nd image
        img2=Image.open(r"Images\facialrecognition.png")
        img2=img2.resize((520,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image = self.photoimg2)
        f_lbl.place(x=520, y=0, width=520, height=100)


        #3rd image
        img3=Image.open(r"Images\jis1.jpg")
        img3=img3.resize((520,100),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image = self.photoimg3)
        f_lbl.place(x=1040, y=0, width=520, height=100)


        #bg image
        img4=Image.open(r"Images\jis3.jpg")
        img4=img4.resize((1540,700),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image = self.photoimg4)
        bg_img.place(x=0, y=100, width=1540, height=730)

        title_lbl = Label(bg_img,text="Student Management System", font=("Times New Roman",25,"bold"), bg="red", fg="white",)
        title_lbl.place(x=0, y=0, width=1540, height=45)


        main_frame = Frame(bg_img,bd=2, bg="white")
        main_frame.place (x=0, y=45, width=1540, height=730)


        #left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Information", font=("times roman",18,"bold"),fg="blue")
        Left_frame.place (x=30, y=10, width=725, height=620)

        img_left=Image.open(r"Images\student2.jpg")
        img_left=img_left.resize((715,100),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image = self.photoimg_left)
        f_lbl.place(x=5, y=0, width=710, height=100)


        #PERSONAL INFO
        personal_info_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Personal Information", font=("times roman",15,"bold"),fg="green")
        personal_info_frame.place (x=5, y=105, width=710, height=145)

        #STUDENT NAME
        studentName_label=Label(personal_info_frame,text="Student Name:",font=("Times New Roman",12,"bold"),bg="white")
        studentName_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(personal_info_frame,textvariable=self.var_name, width=25,font=("Times New Roman",12,"bold"))
        studentName_entry.grid(row=1,column=1,padx=23,pady=5,sticky=W)

        #GENDER
        gender_label=Label(personal_info_frame,text="Gender:",font=("Times New Roman",12,"bold"),bg="white")
        gender_label.grid(row=1,column=2,padx=7,pady=5,sticky=W)

        gender_combo = ttk.Combobox(personal_info_frame,textvariable=self.var_gender, font=("Times New Roman",12,"bold"),width=23,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Transgender")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=20,pady=5,sticky=W)

        #DOB
        dob_label=Label(personal_info_frame,text="DOB:",font=("Times New Roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(personal_info_frame,textvariable=self.var_dob, width=25,font=("Times New Roman",12,"bold"))
        dob_entry.grid(row=2,column=1,padx=23,pady=5,sticky=W)

        #ADDRESS
        address_label=Label(personal_info_frame,text="Address:",font=("Times New Roman",12,"bold"),bg="white")
        address_label.grid(row=2,column=2,padx=8,pady=5,sticky=W)

        address_entry=ttk.Entry(personal_info_frame,textvariable=self.var_address, width=25,font=("Times New Roman",12,"bold"))
        address_entry.grid(row=2,column=3,padx=20,pady=5,sticky=W)

        #Email
        email_label=Label(personal_info_frame,text="Email ID:",font=("Times New Roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(personal_info_frame,textvariable=self.var_email, width=25,font=("Times New Roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=23,pady=5,sticky=W)

        #PHONE NO
        phone_label=Label(personal_info_frame,text="Phone No.:",font=("Times New Roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=8,pady=5,sticky=W)

        phone_entry=ttk.Entry(personal_info_frame,textvariable=self.var_phone, width=25,font=("Times New Roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=20,pady=5,sticky=W)



        #CURRENT COURSE INFORMATION
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=("times roman",15,"bold"),fg="green")
        current_course_frame.place (x=5, y=270, width=710, height=300)

        #department
        dep_label = Label(current_course_frame, text="Department:",font=("Times New Roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep, font=("Times New Roman",12,"bold"),width=23,state="readonly")
        dep_combo["values"]=("Select Department","BBA","BCA","BME","CE","CSE","ECE","EE","IT","ME","MBA","MCA")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Batch
        batch_label=Label(current_course_frame,text="Batch:",font=("Times New Roman",12,"bold"),bg="white")
        batch_label.grid(row=0,column=2,padx=25,pady=5,sticky=W)

        batch_combo=ttk.Combobox(current_course_frame,textvariable=self.var_batch, font=("Times New Roman",12,"bold"),state="readonly",width=23)
        batch_combo["values"]=("Select Batch","2018-2019","2019-2020","2020-2021","2021-2022","2022-2023","2023-2024")
        batch_combo.current(0)
        batch_combo.grid(row=0,column=3,padx=0,pady=5,sticky=W)

        #YEAR
        year_label=Label(current_course_frame,text="Year:",font=("Times New Roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year, font=("Times New Roman",12,"bold"),state="readonly",width=23)
        year_combo["values"]=("Select Year","1st","2nd","3rd","4th")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #SEMESTER
        semester_label=Label(current_course_frame,text="Semester:",font=("Times New Roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=25,pady=5,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_sem, font=("Times New Roman",12,"bold"),state="readonly",width=23)
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=0,pady=5,sticky=W)

        #CLASS DIVISION
        class_div_label=Label(current_course_frame,text="Class Division:",font=("Times New Roman",12,"bold"),bg="white")
        class_div_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        class_div_combo=ttk.Combobox(current_course_frame,textvariable=self.var_div, font=("Times New Roman",12,"bold"),state="readonly",width=23)
        class_div_combo["values"]=("Select Division","Sec-A, Gr-1","Sec-A, Gr-2","Sec-B, Gr-1","Sec-B, Gr-2")
        class_div_combo.current(0)
        class_div_combo.grid(row=2,column=1,padx=5,pady=5,sticky=W)
        
        #STUDENT ID
        studentId_label=Label(current_course_frame,text="Student ID:",font=("Times New Roman",12,"bold"),bg="white")
        studentId_label.grid(row=2,column=2,padx=25,pady=5,sticky=W)

        studentId_entry=ttk.Entry(current_course_frame,textvariable=self.var_id, width=25,font=("Times New Roman",12,"bold"))
        studentId_entry.grid(row=2,column=3,padx=0,pady=5,sticky=W)

        #REGISTRATION NO
        reg_no_label=Label(current_course_frame,text="Registration No.:",font=("Times New Roman",12,"bold"),bg="white")
        reg_no_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        reg_no_entry=ttk.Entry(current_course_frame,textvariable=self.var_reg, width=25,font=("Times New Roman",12,"bold"))
        reg_no_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #ROLL NO
        roll_no_label=Label(current_course_frame,text="Roll No.:",font=("Times New Roman",12,"bold"),bg="white")
        roll_no_label.grid(row=3,column=2,padx=25,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(current_course_frame,textvariable=self.var_roll, width=25,font=("Times New Roman",12,"bold"))
        roll_no_entry.grid(row=3,column=3,padx=0,pady=5,sticky=W)

        #MENTOR NAME
        mentor_label=Label(current_course_frame,text="Mentor Name:",font=("Times New Roman",12,"bold"),bg="white")
        mentor_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        mentor_entry=ttk.Entry(current_course_frame,textvariable=self.var_mentor, width=25,font=("Times New Roman",12,"bold"))
        mentor_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)


        #RADIO BUTTONS
        self.var_radio1=StringVar()
        radiobutton1=ttk.Radiobutton(current_course_frame,variable=self.var_radio1,text="Take A Photo Sample",value="Yes")
        radiobutton1.grid(row=6,column=0)

        radiobutton2=ttk.Radiobutton(current_course_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobutton2.grid(row=6,column=1)
        
        #BUTTONS FRAME
        btn_frame=Frame(current_course_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place (x=0, y=200, width=715, height=70)

        save_btn=Button(btn_frame,text="Save",command=self.add_data, width=18,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data, width=19,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data, width=19,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data, width=18,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(current_course_frame, bd=2, bg="white", relief=RIDGE,)
        btn_frame1.place (x=0, y=235, width=715, height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo Sample",command=self.generate_dataset, width=38,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo Sample",width=39,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)




        #right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", fg="blue", font=("times roman",18,"bold"))
        Right_frame.place (x=780, y=10, width=720, height=620)

        img_right=Image.open(r"Images\student4.jpg")
        img_right=img_right.resize((710,100),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(Right_frame,image = self.photoimg_right)
        f_lbl.place(x=5, y=0, width=706, height=100)


        #================================SEARCH SYSTEM==============================
        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search Student Details", fg="green", font=("times roman",15,"bold"))
        Search_frame.place (x=5, y=105, width=705, height=80)

        search_label=Label(Search_frame,text="Search By",font=("Times New Roman",12,"bold"),bg="red",fg="white",width=12)
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("Times New Roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=17,font=("Times New Roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=12,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)


        showAll_btn=Button(Search_frame,text="Show All",width=12,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        #=================TABLE FRAME====================
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place (x=5, y=210, width=705, height=375)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("name","dep","batch","year","sem","div","id","reg","roll","email","phone","address","gender","dob","mentor","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("name",text="Name")
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("batch",text="Batch")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("id",text="Student_Id")
        self.student_table.heading("reg",text="Registration")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("mentor",text="Mentor")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("name",width=130)
        self.student_table.column("dep",width=100)
        self.student_table.column("batch",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("reg",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("mentor",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    #=================Function Declaration====================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error!", "All Fields Are Required.", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Supali@12",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                    self.var_name.get(),
                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_batch.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_sem.get(),
                                                                                                                    self.var_div.get(),
                                                                                                                    self.var_id.get(),
                                                                                                                    self.var_reg.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_mentor.get(),
                                                                                                                    self.var_radio1.get()

                                                                                                                ))
                conn.commit()
                self.fetch_data
                conn.close()
                messagebox.showinfo("Sucess","Student Details Has Been Added Successfully.",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error!",f"Due To :{str(es)}",parent=self.root)



    #===================fatch data==================
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Supali@12",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


#===================get cursor===================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_name.set(data[0]),
        self.var_dep.set(data[1]),
        self.var_batch.set(data[2]),
        self.var_year.set(data[3]),
        self.var_sem.set(data[4]),
        self.var_div.set(data[5]),
        self.var_id.set(data[6]),
        self.var_reg.set(data[7]),
        self.var_roll.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_address.set(data[11]),
        self.var_gender.set(data[12]),
        self.var_dob.set(data[13]),
        self.var_mentor.set(data[14]),
        self.var_radio1.set(data[15])



    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error!", "All Fields Are Required.", parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update!","Do You Really Want To Update The Student Details?",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Supali@12",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update Student Set Name=%s,Department=%s,Batch=%s,Year=%s,Semester=%s,Division=%s,Registration=%s,Roll=%s,Email=%s,Phone=%s,Address=%s,Gender=%s,DOB=%s,Mentor=%s,PhotoSampleStatus=%s where Student_Id=%s",(
                                                                                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                                                        self.var_batch.get(),
                                                                                                                                                                                                                                                        self.var_year.get(),
                                                                                                                                                                                                                                                        self.var_sem.get(),
                                                                                                                                                                                                                                                        self.var_div.get(),
                                                                                                                                                                                                                                                        self.var_reg.get(),
                                                                                                                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                                                        self.var_mentor.get(),
                                                                                                                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                                                                                                                        self.var_id.get()
                                                                                                                                                                                                                                                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Sucess","Student Details Updated Successfully.",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error!",f"Due To:{str(es)}",parent=self.root)


    #delete function
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error!","Student ID Must Be Required.",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Deletion!","Do You Really Want To Delete The Student?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Supali@12",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_Id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Sucessfully Deleted Student Details.",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error!",f"Due To:{str(es)}",parent=self.root)

     # reset 
    def reset_data(self):
        self.var_name.set("")
        self.var_dep.set("Select Deperment")
        self.var_batch.set("Select Batch")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_div.set("Select Division")
        self.var_id.set("")
        self.var_reg.set("")
        self.var_roll.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_mentor.set("")
        self.var_radio1.set("")

    #=================Generate data set or take photo Samples ===================
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()==""or self.var_id.get()=="":
            messagebox.showerror("Error!","All Fields are required.",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Supali@12",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("Update student set Name=%s,Department=%s,Batch=%s,Year=%s,Semester=%s,Division=%s,Registration=%s,Roll=%s,Email=%s,Phone=%s,Address=%s,Gender=%s,DOB=%s,Mentor=%s,PhotoSampleStatus=%s where Student_Id=%s",(
                                                                                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                                                self.var_batch.get(),
                                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                                self.var_sem.get(),
                                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                                self.var_reg.get(),
                                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                                self.var_mentor.get(),
                                                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                                                self.var_id.get()
                                                                                                                                                                                                                                
                                                                                                                                                                                                                                
                                                                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()



                #================load predifine data on face frontals from opencv==================
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbor=5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(650,650))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int (img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Completed.",parent=self.root)
            except Exception as es:
              messagebox.showerror("Error!",f"Due To:{str(es)}",parent=self.root)




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

        b1=Button(bg_img,image = self.photoimg7, cursor="hand2")
        b1.place(x=810, y=110, width=220, height=220)

        b1_1=Button(bg_img, text = "Attendance", cursor="hand2", font=("Helvetica",20,"bold"), bg="dark blue", fg="white")
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
        b1.place(x=150, y=410, width=220, height=220)

        b1_1=Button(bg_img, text = "Gallery", cursor="hand2", command=self.open_img, font=("Helvetica",20,"bold"), bg="dark blue", fg="white")
        b1_1.place(x=150, y=610, width=220, height=40)


        #ChatBot button
        img10=Image.open(r"Images\chatbot.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image = self.photoimg10, cursor="hand2",command=self.chatbot)
        b1.place(x=480, y=410, width=220, height=220)

        b1_1=Button(bg_img, text = "ChatBot", cursor="hand2",command=self.chatbot, font=("Helvetica",20,"bold"), bg="dark blue", fg="white")
        b1_1.place(x=480, y=610, width=220, height=40)


        #Developers button
        img11=Image.open(r"Images\dev.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image = self.photoimg11,command=self.developer_data, cursor="hand2")
        b1.place(x=810, y=410, width=220, height=220)

        b1_1=Button(bg_img, text = "Developers",command=self.developer_data, cursor="hand2", font=("Helvetica",20,"bold"), bg="dark blue", fg="white")
        b1_1.place(x=810, y=610, width=220, height=40)


        #Exit button
        img12=Image.open(r"Images\exit.jpg")
        img12=img12.resize((220,220),Image.ANTIALIAS)
        self.photoimg12=ImageTk.PhotoImage(img12)

        b1=Button(bg_img,image = self.photoimg12, command=self.iExit, cursor="hand2")
        b1.place(x=1140, y=410, width=220, height=220)

        b1_1=Button(bg_img, text = "Exit", cursor="hand2",command=self.iExit, font=("Helvetica",20,"bold"), bg="dark blue", fg="white")
        b1_1.place(x=1140, y=610, width=220, height=40)


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

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def chatbot(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)

    def train(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)





if __name__ == "__main__":
    main()