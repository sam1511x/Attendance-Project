from tkinter import * 
from tkinter import ttk 
from PIL import Image, ImageTk
from time import strftime
from datetime import datetime
import os
from student import student
from train import Train
from face_recognition import face_recognition
from attendance import attendance

class Face_Recognition :
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition")

        # Background Image
        img1 = Image.open(r"C:\Users\Sam\Desktop\Face Recognition Project\Images\BGI.jpeg")
        img1 = img1.resize((1800,1000))
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=0,y=0,width=1800,height=1000)

        # Label 
        title_lbl = Label(f_lbl1, text="ATTENDANCE VIA FACE RECOGNITION", font=("Times New Roman", 30, "bold"), fg="black", bg="white")
        title_lbl.place(x=430, y=30)

        # Student Details Button
        img2 = Image.open(r"C:\Users\Sam\Desktop\Face Recognition Project\Images\StudentButtonBGI.png")
        img2 = img2.resize((150,150))
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b1 = Button(f_lbl1, image=self.photoimg2,command=self.student_details, cursor="hand2")
        b1.place(x=300, y=130, width=150, height=150)

        b1_1 = Button(f_lbl1, text="Student Details",command=self.student_details, cursor="hand2",font=("Times New Roman", 15, "bold"), fg="white", bg="darkblue")
        b1_1.place(x=300, y=250, width=150, height=40)

        # Face Detection Button
        img3 = Image.open(r"C:\Users\Sam\Desktop\Face Recognition Project\Images\FaceDetectorButtonBGI.jpeg")
        img3 = img3.resize((150,150))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b1 = Button(f_lbl1, image=self.photoimg3, cursor="hand2",command=self.face_data)
        b1.place(x=300, y=330, width=150, height=150)

        b1_1 = Button(f_lbl1, text="Face Detector", cursor="hand2",command=self.face_data,font=("Times New Roman", 15, "bold"), fg="white", bg="darkblue")
        b1_1.place(x=300, y=450, width=150, height=40)

        # Attendance Button
        img4 = Image.open(r"C:\Users\Sam\Desktop\Face Recognition Project\Images\AttendanceButtonBGI.jpeg")
        img4 = img4.resize((150,150))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(f_lbl1, image=self.photoimg4, cursor="hand2",command=self.attendance_data)
        b1.place(x=300, y=530, width=150, height=150)

        b1_1 = Button(f_lbl1, text="Attendance", cursor="hand2",command=self.attendance_data,font=("Times New Roman", 15, "bold"), fg="white", bg="darkblue")
        b1_1.place(x=300, y=650, width=150, height=40)

        # Train Data Button
        img5 = Image.open(r"C:\Users\Sam\Desktop\Face Recognition Project\Images\TrainDataButtonBGI.jpeg")
        img5 = img5.resize((150,150))
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(f_lbl1, image=self.photoimg5, cursor="hand2",command=self.train_data )
        b1.place(x=1200, y=130, width=150, height=150)

        b1_1 = Button(f_lbl1, text="Train Data", cursor="hand2",command=self.train_data, font=("Times New Roman", 15, "bold"), fg="white", bg="darkblue")
        b1_1.place(x=1200, y=250, width=150, height=40)

        # Photos Button
        img6 = Image.open(r"C:\Users\Sam\Desktop\Face Recognition Project\Images\PhotosButtonBGI.jpg")
        img6 = img6.resize((150,150))
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(f_lbl1, image=self.photoimg6, cursor="hand2",command=self.open_img)
        b1.place(x=1200, y=330, width=150, height=150)

        b1_1 = Button(f_lbl1, text="Photos", cursor="hand2",command=self.open_img,font=("Times New Roman", 15, "bold"), fg="white", bg="darkblue")
        b1_1.place(x=1200, y=450, width=150, height=40)

        # Exit Button
        img7 = Image.open(r"C:\Users\Sam\Desktop\Face Recognition Project\Images\ExitButttonBGI.jpeg")
        img7 = img7.resize((150,150))
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(f_lbl1, image=self.photoimg7, cursor="hand2", command=self.exit)
        b1.place(x=1200, y=530, width=150, height=150)

        b1_1 = Button(f_lbl1, text="Exit", cursor="hand2", command=self.exit,font=("Times New Roman", 15, "bold"), fg="white", bg="darkblue")
        b1_1.place(x=1200, y=650, width=150, height=40)

    def open_img(self):
        os.startfile(r"C:\Users\Sam\Desktop\Face Recognition Project\Data")

    def exit(self):
        self.root.destroy()

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=face_recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
