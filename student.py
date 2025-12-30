from tkinter import * 
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class student :
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Student Details")


        # Variables 
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_dept=StringVar()
        self.var_batch=StringVar()
        self.var_sem=StringVar()
        self.var_mail=StringVar()
        self.var_gender=StringVar()
        self.var_DOB=StringVar() 
       
        # Background Image
        img8 = Image.open(r"C:\Users\Sam\Desktop\Face Recognition Project\Images\SubBGI.jpeg")
        img8 = img8.resize((1800,1000))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        f_lbl2 = Label(self.root, image=self.photoimg8)
        f_lbl2.place(x=0,y=0,width=1800,height=1000)

        # Label 
        title_lbl2 = Label(f_lbl2, text="STUDENT DETAILS", font=("Times New Roman", 30, "bold"), fg="black", bg="white")
        title_lbl2.place(x=550, y=30)

        main_frame = Frame(f_lbl2, bd=2)
        main_frame.place(x=50,y=100,width=1420,height=650)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Details",font=("Times New Roman",12,"bold"))
        left_frame.place(x=20,y=10,width=670,height=610)

        # Current Course 
        current_course = LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Academic Details",font=("Times New Roman",12,"bold"))
        current_course.place(x=10,y=5,width=650,height=210)

        # Course Combobox
        course_label = Label(current_course,text="Course", font=("Times New Roman", 12, "bold"))
        course_label.grid(row=0,column=0,padx=10)

        course_combo = ttk.Combobox(current_course,textvariable=self.var_course,font=("Times New Roman", 12, "bold"), width=17,state="read only")
        course_combo["values"]=("Select Course","BS-MS","BS","MS","PhD","iPhD")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=2,pady=10)

        # Department Combobox
        dep_label = Label(current_course,text="Department", font=("Times New Roman", 12, "bold"))
        dep_label.grid(row=1,column=0,padx=10)

        dep_combo = ttk.Combobox(current_course,textvariable=self.var_dept,font=("Times New Roman", 12, "bold"), width=17,state="read only")
        dep_combo["values"]=("Select Department","Biological Sciences","Chemical Engineering","Chemistry","Data Science and Engineering","Earth and Environmental Sciences","Economics","Electrical Engineering and Computer Science","Humanities and Social Sciences","Mathematics","Physics")
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10)

        # Year Combobox
        year_label = Label(current_course,text="Batch", font=("Times New Roman", 12, "bold"))
        year_label.grid(row=2,column=0,padx=10)

        year_combo = ttk.Combobox(current_course,textvariable=self.var_batch,font=("Times New Roman", 12, "bold"), width=17,state="read only")
        year_combo["values"]=("Select Batch","25","24","23","22","21","20","19")
        year_combo.current(0)
        year_combo.grid(row=2,column=1,padx=2,pady=10)

        # Semester Combobox
        sem_label = Label(current_course,text="Semester", font=("Times New Roman", 12, "bold"))
        sem_label.grid(row=3,column=0,padx=10)

        sem_combo = ttk.Combobox(current_course,textvariable=self.var_sem,font=("Times New Roman", 12, "bold"), width=17,state="read only")
        sem_combo["values"]=("Select Semester","Odd","Even")
        sem_combo.current(0)
        sem_combo.grid(row=3,column=1,padx=2,pady=10)

        # Student Details
        student_details = LabelFrame(left_frame,bd=2,relief=RIDGE,text="Student Information Details",font=("Times New Roman",12,"bold"))
        student_details.place(x=10,y=220,width=650,height=360)

        # Roll No. Combobox
        roll_label = Label(student_details,text="RollNo", font=("Times New Roman", 12, "bold"))
        roll_label.grid(row=0,column=0,padx=10,sticky=W,pady=10)

        roll_entry =ttk.Entry(student_details,textvariable=self.var_roll, width = 20, font=("Times New Roman", 12, "bold"))
        roll_entry.grid(row=0,column=1,padx=10,sticky=W,pady=10)

        # Name Combobox
        name_label = Label(student_details,text="Name", font=("Times New Roman", 12, "bold"))
        name_label.grid(row=1,column=0,padx=10,sticky=W,pady=10)

        name_entry =ttk.Entry(student_details,textvariable=self.var_name, width = 20, font=("Times New Roman", 12, "bold"))
        name_entry.grid(row=1,column=1,padx=10,sticky=W,pady=10)

        # Email Combobox
        mail_label = Label(student_details,text="Email", font=("Times New Roman", 12, "bold"))
        mail_label.grid(row=2,column=0,padx=10,sticky=W,pady=10)

        mail_entry =ttk.Entry(student_details,textvariable=self.var_mail, width = 20, font=("Times New Roman", 12, "bold"))
        mail_entry.grid(row=2,column=1,padx=10,sticky=W,pady=10)

        # Gender Combobox
        gen_label = Label(student_details,text="Gender", font=("Times New Roman", 12, "bold"))
        gen_label.grid(row=3,column=0,padx=10,sticky=W,pady=10)

        gen_combo = ttk.Combobox(student_details,textvariable=self.var_gender,font=("Times New Roman", 12, "bold"), width=17,state="read only")
        gen_combo["values"]=("Select Gender","Male","Female","Other")
        gen_combo.current(0)
        gen_combo.grid(row=3,column=1,padx=10,sticky=W,pady=10)

        # D.O.B Combobox
        dob_label = Label(student_details,text="Date of Birth", font=("Times New Roman", 12, "bold"))
        dob_label.grid(row=4,column=0,padx=10,sticky=W,pady=10)

        dob_entry =ttk.Entry(student_details,textvariable=self.var_DOB, width = 20, font=("Times New Roman", 12, "bold"))
        dob_entry.grid(row=4,column=1,padx=10,sticky=W,pady=10)

        # Radio Buttons 
        self.var_radio1=StringVar()
        radiobutton1 = ttk.Radiobutton(student_details,variable=self.var_radio1,text="Take Photo Sample", value="Yes")
        radiobutton1.grid(row=5,column=0,padx=10)

        radiobutton2 = ttk.Radiobutton(student_details,variable=self.var_radio1,text="No Photo Sample", value="No")
        radiobutton2.grid(row=5,column=1,padx=10)

        # Buttons Frame
        btn_frame = Frame(student_details,bd=2,relief=RIDGE)
        btn_frame.place(x=15,y=260,width=620,height=30)

        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=16,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=16,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=16,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn2_frame = Frame(student_details,bd=2,relief=RIDGE)
        btn2_frame.place(x=15,y=290,width=620,height=30)

        take_btn = Button(btn2_frame,text="Take Photo Sample",command=self.generate_dataset,width=35,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        take_btn.grid(row=0,column=0)

        up_btn = Button(btn2_frame,text="Update Photo Sample",width=35,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        up_btn.grid(row=0,column=1)


        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Data",font=("Times New Roman",12,"bold"))
        right_frame.place(x=700,y=10,width=690,height=610)

        # Searching Part 
        search_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,text="Searching Part",font=("Times New Roman",12,"bold"))
        search_frame.place(x=5,y=10,width=680,height=70)

        search_label = Label(search_frame,text="Search By", font=("Times New Roman", 15, "bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,sticky=W,pady=10)

        search_combo = ttk.Combobox(search_frame,font=("Times New Roman", 12, "bold"), width=15,state="read only")
        search_combo["values"]=("Select","RollNo","Name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry =ttk.Entry(search_frame, width = 20, font=("Times New Roman", 12, "bold"))
        search_entry.grid(row=0,column=2,padx=3,sticky=W,pady=10)

        search_btn = Button(search_frame,text="Search",width=13,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2)

        show_btn = Button(search_frame,text="Show All",width=13,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        show_btn.grid(row=0,column=4,padx=2)

        # Table Frame
        table_frame = Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=90,width=680,height=480)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("roll","name","course","dept","batch","sem","mail","gender","DOB","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("roll",text="RollNo")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("dept",text="Department")
        self.student_table.heading("batch",text="Batch")
        self.student_table.heading("sem",text="Semester")    
        self.student_table.heading("mail",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("DOB",text="DateOfBirth")
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("roll",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("dept",width=100)
        self.student_table.column("batch",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("mail",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("photo",width=150)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    def add_data(self):
        if self.var_roll.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Zxcvbnm.1",database="face_recognizer")
                my_cursor=conn.cursor()
                
                my_cursor.execute("Insert into student value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_dept.get(),
                    self.var_batch.get(),
                    self.var_sem.get(),
                    self.var_mail.get(),
                    self.var_gender.get(),
                    self.var_DOB.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Students details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # Fetch Data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Zxcvbnm.1",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * From student")
        data=my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    # FIXED: Added proper error handling for empty data
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        # Check if data exists and has enough elements
        if data and len(data) >= 10:
            self.var_roll.set(data[0])
            self.var_name.set(data[1])
            self.var_course.set(data[2])
            self.var_dept.set(data[3])
            self.var_batch.set(data[4])
            self.var_sem.set(data[5])
            self.var_mail.set(data[6])
            self.var_gender.set(data[7])
            self.var_DOB.set(data[8])
            self.var_radio1.set(data[9])

    # Update
    def update_data(self):
        if self.var_roll.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Zxcvbnm.1",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Name=%s, Course=%s, Department=%s, Batch=%s, Semester=%s, Email=%s, Gender=%s, DateOfBirth=%s, PhotoSample=%s where RollNo=%s",(
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_dept.get(),
                        self.var_batch.get(),
                        self.var_sem.get(),
                        self.var_mail.get(),
                        self.var_gender.get(),
                        self.var_DOB.get(),
                        self.var_radio1.get(),
                        self.var_roll.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)

    # Delete
    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","RollNo must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Zxcvbnm.1",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where RollNo=%s"
                    val=(self.var_roll.get(),)
                    my_cursor.execute(sql,val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
                else:
                    return
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)

    # Reset 
    def reset_data(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_course.set("Select Course")
        self.var_dept.set("Select Department")
        self.var_batch.set("Select Batch")
        self.var_sem.set("Select Semester")
        self.var_mail.set("")
        self.var_gender.set("Select Gender")
        self.var_DOB.set("")
        self.var_radio1.set("")

    # Generate Data Set (Collecting Photos)
    def generate_dataset(self):
        if self.var_roll.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Zxcvbnm.1",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("Select * From student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id += 1
                my_cursor.execute("Update student set Name=%s, Course=%s, Department=%s, Batch=%s, Semester=%s, Email=%s, Gender=%s, DateOfBirth=%s, PhotoSample=%s where RollNo=%s",(
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_dept.get(),
                    self.var_batch.get(),
                    self.var_sem.get(),
                    self.var_mail.get(),
                    self.var_gender.get(),
                    self.var_DOB.get(),
                    self.var_radio1.get(),
                    self.var_roll.get()
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
                # Load Predefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier(r"C:\Users\Sam\Desktop\Face Recognition Project\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path=r"C:\Users\Sam\Desktop\Face Recognition Project\Data\user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Dataset Completed !!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()