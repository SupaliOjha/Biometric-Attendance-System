from tkinter import*
from PIL import Image,ImageTk
import mysql.connector
from datetime import datetime
import cv2 
import face_recognition
import numpy.random as npr


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Biometric Attendance System")


        title_lbl = Label(self.root,text="FACE RECOGNITION", font=("times New Roman",35,"bold"),bg="white",fg="navy blue",)
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # 1st image
        img_left=Image.open(r"Images/face_detector.jpg")
        img_left=img_left.resize((670,755),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=0,y=55,width=670,height=755)

        # 2nd image
        img_right=Image.open(r"Images/facial_recognition.jpg")
        img_right=img_right.resize((950,755),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=670,y=55,width=950,height=755)

        # Button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2", command=self.face_recog,font=("times new roman",22,"bold"),bg="blue",fg="white")
        b1_1.place(x=345, y=670, width=250, height=50)

    #========================attendance========================
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    #==========================face recognition==========================

    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Supali@12",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_Id="+str(id))
                n=my_cursor.fetchone()
                #n="+".join(n)

                my_cursor.execute("select Roll from student where Student_Id="+str(id))
                r=my_cursor.fetchone()
                #r="+".join(r)

                my_cursor.execute("select Department from student where Student_Id="+str(id))
                d=my_cursor.fetchone()
                #d="+".join(d)

                my_cursor.execute("select Student_Id from student where Student_Id="+str(id))
                i=my_cursor.fetchone()
                #i="+".join(i)

                if confidence>77:
                    cv2.putText(img, f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img, f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)
            
            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()