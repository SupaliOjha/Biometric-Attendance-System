from pathlib import WindowsPath
from tkinter import*
from tkinter import ttk
from typing import Pattern
from PIL import Image,ImageTk
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Biometric Attendance System")


        #=========variables==============
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_attendance=StringVar()

        #1st image
        img1=Image.open(r"Images/attendance.jpg")
        img1=img1.resize((760,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=760, height=200)


        #2nd image
        img2=Image.open(r"Images/attendance1.jpg")
        img2=img2.resize((790,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=760, y=0, width=790, height=150)

        #bg image
        img4=Image.open(r"Images/facerecog.png")
        img4=img4.resize((1540,700),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image = self.photoimg4)
        bg_img.place(x=0, y=150, width=1540, height=730)

        title_lbl = Label(bg_img,text="Attendance Management System", font=("Times New Roman",25,"bold"), fg="white", bg="green")
        title_lbl.place(x=0, y=0, width=1540, height=45)

        #================time=================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl = Label(title_lbl, font=('times new roman',20,'bold'), bg='green',fg='white')
        lbl.place(x=1320,y=-5,width=210,height=50)
        time()


        main_frame = Frame(bg_img,bd=2, bg="white")
        main_frame.place (x=30, y=75, width=1470, height=550)

        #left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman",22,"bold"),fg="dark green")
        Left_frame.place (x=30, y=10, width=720, height=500)

        img_left=Image.open(r"Images/facerecog.png")
        img_left=img_left.resize((720,160),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image = self.photoimg_left)
        f_lbl.place(x=5, y=0, width=710, height=160)

        left_inside_frame = Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place (x=5, y=175, width=710, height=290)

        #Labels and entry
        #Name
        attendanceId_label=Label(left_inside_frame,text="Name",font=("Times New Roman",15,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("Times New Roman",15,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=8,sticky=W)

        #Department
        rollLabel_label=Label(left_inside_frame,text="Department",font=("Times New Roman",15,"bold"),bg="white")
        rollLabel_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("Times New Roman",15,"bold"))
        atten_roll.grid(row=0,column=3,pady=8)

        #ID
        nameLabel=Label(left_inside_frame,text="Student ID",font=("Times New Roman",15,"bold"),bg="white")
        nameLabel.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("Times New Roman",15,"bold"))
        atten_roll.grid(row=1,column=1,pady=8)

        #roll
        depLabel=Label(left_inside_frame,text="Roll",font=("Times New Roman",15,"bold"),bg="white")
        depLabel.grid(row=1,column=2)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("Times New Roman",15,"bold"))
        atten_roll.grid(row=1,column=3,pady=8)

        #Date
        timeLabel_label=Label(left_inside_frame,text="Date",font=("Times New Roman",15,"bold"),bg="white")
        timeLabel_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("Times New Roman",15,"bold"))
        atten_roll.grid(row=2,column=1,pady=8)

        #Time
        dateLabel_label=Label(left_inside_frame,text="Time",font=("Times New Roman",15,"bold"),bg="white")
        dateLabel_label.grid(row=2,column=2)

        atten_roll=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("Times New Roman",15,"bold"))
        atten_roll.grid(row=2,column=3,pady=8)

        #attendance
        attendanceLabel=Label(left_inside_frame,text="Status",font=("Times New Roman",15,"bold"),bg="white")
        attendanceLabel.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,textvariable=self.var_atten_attendance,font=("Times New Roman",15,"bold"),state="readonly",width=18)
        self.atten_status["values"]=("Select","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #BUTTONS FRAME
        btn_frame=Frame(left_inside_frame, bd=2, bg="white", relief=RIDGE,)
        btn_frame.place (x=0, y=250, width=740, height=35)

        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv, width=14,font=("times new roman",15,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv, width=14,font=("times new roman",15,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Update", width=14,font=("times new roman",15,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data, width=14,font=("times new roman",15,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        #right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman",22,"bold"),fg="dark green")
        Right_frame.place (x=780, y=10, width=655, height=500)

        table_frame=Frame(Right_frame, bd=2, bg="white", relief=RIDGE,)
        table_frame.place (x=5, y=5, width=645, height=460)

        #================scroll bar table======================
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendaceReportTable=ttk.Treeview(table_frame,column=("name","deparment","id","roll","date","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)

        self.AttendaceReportTable.heading("name",text="Name")
        self.AttendaceReportTable.heading("deparment",text="Deparment")
        self.AttendaceReportTable.heading("id",text="Attendance ID")
        self.AttendaceReportTable.heading("roll",text="Roll")
        self.AttendaceReportTable.heading("date",text="Date")    
        self.AttendaceReportTable.heading("time",text="Time")
        self.AttendaceReportTable.heading("attendance",text="Attendance")

        self.AttendaceReportTable["show"]="headings"
        self.AttendaceReportTable.column("name",width=100)
        self.AttendaceReportTable.column("deparment",width=100)
        self.AttendaceReportTable.column("id",width=100)
        self.AttendaceReportTable.column("roll",width=100)
        self.AttendaceReportTable.column("date",width=100)
        self.AttendaceReportTable.column("time",width=100)
        self.AttendaceReportTable.column("attendance",width=100)

        
        self.AttendaceReportTable.pack(fill=BOTH,expand=1)

        self.AttendaceReportTable.bind("<ButtonRelease>",self.get_cursor)


    #==========fetch data==========
    def fetchData(self,rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("",END,values=i)
    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),titel="Open CSV", filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    #export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","NO Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),titel="Open CSV", filetypes=(("CSV file","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data Exported to"+os.path.basename(fln)+"Successfully",parent=self.root)

        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    def get_cursor(self,event=""):
        cursor_row=self.AttendaceReportTable.focus()
        content=self.AttendaceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_name.set(rows[0])
        self.var_atten_dep.set(rows[1])
        self.var_atten_id.set(rows[2])
        self.var_atten_roll.set(rows[3])
        self.var_atten_date.set(rows[4])
        self.var_atten_time.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_date.set("")
        self.var_atten_time.set("")
        self.var_atten_attendance.set("")








if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()