from tkinter import * 
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class face_recognition :
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition")

        img8 = Image.open(r"C:\Users\Sam\Desktop\Face Recognition Project\Images\SubBGI.jpeg")
        img8 = img8.resize((1800,1000))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        lbl = Label(self.root, image=self.photoimg8)
        lbl.place(x=0,y=0,width=1800,height=1000)

        title_lbl = Label(lbl, text="FACE RECOGNITION", font=("Times New Roman", 30, "bold"), fg="black", bg="gray")
        title_lbl.place(x=610, y=30)

        b1_1 = Button(lbl, text="FACE DETECTOR",cursor="hand2",command=self.face_reco,font=("Times New Roman", 40, "bold"), fg="white", bg="darkblue")
        b1_1.place(x=70, y=300, width=1370, height=100)

    # Face Recognition 
    def face_reco(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord = []
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="Zxcvbnm.1",database="face_recognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("SELECT RollNo FROM student WHERE RollNo="+str(id))
                r = my_cursor.fetchone()
                r = str(r[0]) if r else "Unknown"  # Fixed: Extract the value from tuple

                my_cursor.execute("SELECT Name FROM student WHERE RollNo="+str(id))
                n = my_cursor.fetchone()
                n = str(n[0]) if n else "Unknown"  # Fixed: Extract the value from tuple

                conn.close()  # Added: Close the connection

                if confidence>77:
                    cv2.putText(img,f"RollNo:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Person",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier(r"C:\Users\Sam\Desktop\Face Recognition Project\haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = face_recognition(root)
    root.mainloop()  # Fixed: Added parentheses to actually call mainloop