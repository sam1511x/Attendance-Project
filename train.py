from tkinter import * 
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train :
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Train Data")

        img8 = Image.open(r"C:\Users\Sam\Desktop\Face Recognition Project\Images\SubBGI.jpeg")
        img8 = img8.resize((1800,1000))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        lbl = Label(self.root, image=self.photoimg8)
        lbl.place(x=0,y=0,width=1800,height=1000)

        title_lbl = Label(lbl, text="TRAIN DATA", font=("Times New Roman", 30, "bold"), fg="black", bg="gray")
        title_lbl.place(x=630, y=30)

        b1_1 = Button(lbl, text="TRAIN DATA NOW",command=self.train_classifier,cursor="hand2",font=("Times New Roman", 40, "bold"), fg="white", bg="darkblue")
        b1_1.place(x=70, y=300, width=1370, height=100)

    def train_classifier(seld):
        data_dir=(r"C:\Users\Sam\Desktop\Face Recognition Project\Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')     #Gray Scale Image
            img_np=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(img_np)
            ids.append(id)
            cv2.imshow("Training",img_np)
            cv2.waitKey(1)==13
        ids=np.array(ids)

    # Train the Classifier 
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed !!")



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()