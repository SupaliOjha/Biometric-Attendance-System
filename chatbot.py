from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk



class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("ChatBot")
        self.root.bind('<Return>',self.enter_func)

        main_frame = Frame(self.root,bd=4, bg="light green",width=1520)
        main_frame.pack()

        img_chat=Image.open(r"Images\chatbot.jpg")
        img_chat=img_chat.resize((150,90),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=2, relief=RAISED, anchor='nw', width=1520, compound=LEFT, image = self.photoimg, text='Chat Me',font=("arial",30,"bold"), fg="green", bg="white")
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=1400,height=26,bd=3,relief=RAISED,font=("arial",15), yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root, bd=2, bg="white", width=1400)
        btn_frame.pack()

        label1=Label(btn_frame,text="Type Something",font=("arial",15,"bold"),bg="white",fg="green")
        label1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=("arial",16))
        self.entry.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send",command=self.send,font=("arial",16,"bold"),width=6,bg="green",fg="white")
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear",command=self.clear, font=("arial",16,"bold"),width=6,bg="red",fg="white")
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label2=Label(btn_frame,text=self.msg,font=("arial",15,"bold"),bg="white",fg="green")
        self.label2.grid(row=1,column=1,padx=5,sticky=W)


    #===============Function declaration===============
    
    def enter_func(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    def send(self):
        send='\t\t\t\t\t\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg="Please Enter Some Input"
            self.label2.config(text=self.msg,fg="red")

        else:
            self.msg=''
            self.label2.config(text=self.msg,fg="red")

            if(self.entry.get()=="Hello"):
                self.text.insert(END,'\n\n'+'Bot: Hi!')

            elif(self.entry.get()=="Hi"):
                self.text.insert(END,'\n\n'+'Bot: Hello!')

            elif(self.entry.get()=="How are you?"):
                self.text.insert(END,'\n\n'+'Bot: Fine, and you?')

            elif(self.entry.get()=="Fantastic"):
                self.text.insert(END,'\n\n'+'Bot: Nice to hear.')

            elif(self.entry.get()=="How does facial recognition work?"):
                self.text.insert(END,'\n\n'+'Bot: Step \n1: Face detection - The camera detects and locates the image of a face, either alone or in a crowd.\nStep 2: Face analysis - Next, an image of the face is captured and analyzed.\nStep 3: Converting the image to data.\nStep 4: Finding a match.')                

            elif(self.entry.get()=="How does face recognition attendance system work?"):
                self.text.insert(END,'\n\n'+"Bot: A facial recognition attendance system uses facial recognition technology to identify and verify a person using the person's facial features and automatically mark attendance.")

            elif(self.entry.get()=="How do you use the face recognition attendance system in Python?"):
                self.text.insert(END,'\n\n'+'Bot: \n1. Install Python and dependencies. Follow this in the documentation.\n2. Install OpenCV along with python wrappers.\n3. Install numpy using pip install numpy.\n4. Install requests using pip install requests.\n5. Create a file attendance.py and start coding as follows.')

            elif(self.entry.get()=="Okay, Bye"):
                self.text.insert(END,'\n\n'+'Bot: Thank you for chatting.')

            else:
                self.text.insert(END,'\n\n'+"Bot: Sorry, I didn't get it.")

                                               



if __name__ == "__main__":
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()