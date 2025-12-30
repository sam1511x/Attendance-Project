from tkinter import * 
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class attendance :
    def __init__(self,root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Attendance")

        # Variables
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_dept = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_status = StringVar()
        

        img8 = Image.open(r"C:\Users\Sam\Desktop\Face Recognition Project\Images\SubBGI.jpeg")
        img8 = img8.resize((1800,1000))
        self.photoimg8 = ImageTk.PhotoImage(img8)

        lbl = Label(self.root, image=self.photoimg8)
        lbl.place(x=0,y=0,width=1800,height=1000)

        title_lbl = Label(lbl, text="ATTENDANCE", font=("Times New Roman", 30, "bold"), fg="black", bg="gray")
        title_lbl.place(x=630, y=30)

        main_frame = Frame(lbl, bd=2)
        main_frame.place(x=50,y=150,width=1420,height=450)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("Times New Roman",12,"bold"))
        left_frame.place(x=20,y=10,width=670,height=430)

        left_in_frame = Frame(left_frame, bd=2, relief=RIDGE)
        left_in_frame.place(x=10,y=10,width=650,height=380)

        # Labels & Entry
        roll_label = Label(left_in_frame,text="RollNo", font=("Times New Roman", 12, "bold"))
        roll_label.grid(row=1,column=0,padx=10,sticky=W,pady=10)

        roll_entry =ttk.Entry(left_in_frame,width = 20, textvariable=self.var_roll, font=("Times New Roman", 12, "bold"))
        roll_entry.grid(row=1,column=1,padx=10,sticky=W,pady=10)

        name_label = Label(left_in_frame,text="Name", font=("Times New Roman", 12, "bold"))
        name_label.grid(row=2,column=0,padx=10,sticky=W,pady=10)

        name_entry =ttk.Entry(left_in_frame,width = 20, textvariable=self.var_name, font=("Times New Roman", 12, "bold"))
        name_entry.grid(row=2,column=1,padx=10,sticky=W,pady=10)

        dept_label = Label(left_in_frame,text="Department", font=("Times New Roman", 12, "bold"))
        dept_label.grid(row=3,column=0,padx=10,sticky=W,pady=10)

        dept_entry =ttk.Entry(left_in_frame,width = 20, textvariable=self.var_dept, font=("Times New Roman", 12, "bold"))
        dept_entry.grid(row=3,column=1,padx=10,sticky=W,pady=10)

        time_label = Label(left_in_frame,text="Time", font=("Times New Roman", 12, "bold"))
        time_label.grid(row=4,column=0,padx=10,sticky=W,pady=10)

        time_entry =ttk.Entry(left_in_frame,width = 20, textvariable=self.var_time, font=("Times New Roman", 12, "bold"))
        time_entry.grid(row=4,column=1,padx=10,sticky=W,pady=10)

        date_label = Label(left_in_frame,text="Date", font=("Times New Roman", 12, "bold"))
        date_label.grid(row=5,column=0,padx=10,sticky=W,pady=10)

        date_entry =ttk.Entry(left_in_frame,width = 20, textvariable=self.var_date, font=("Times New Roman", 12, "bold"))
        date_entry.grid(row=5,column=1,padx=10,sticky=W,pady=10)

        status_label = Label(left_in_frame,text="AttendanceStatus", font=("Times New Roman", 12, "bold"))
        status_label.grid(row=6,column=0,padx=10,sticky=W,pady=10)

        status_combo = ttk.Combobox(left_in_frame,font=("Times New Roman", 12, "bold"), width=17, textvariable=self.var_status, state="read only")
        status_combo["values"]=("Status","Present","Absent")
        status_combo.current(0)
        status_combo.grid(row=6,column=1,padx=10,sticky=W,pady=10)

        # Button
        btn_frame = Frame(left_in_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=7,y=325,width=610,height=30)

        import_btn = Button(btn_frame,text="Import CSV",command=self.importcsv,width=16,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn = Button(btn_frame,text="Export CSV",command=self.exportcsv,width=16,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn = Button(btn_frame,text="Update",width=16,font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",width=16,command=self.reset_data, font=("Times New Roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("Times New Roman",12,"bold"))
        right_frame.place(x=700,y=10,width=690,height=430)

        right_in_frame = Frame(right_frame, bd=2, relief=RIDGE)
        right_in_frame.place(x=10,y=10,width=670,height=380)

        # Scroll Bar
        table_frame = Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=10,y=10,width=670,height=380)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendancetable=ttk.Treeview(table_frame, column=("roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendancetable.xview)
        scroll_y.config(command=self.attendancetable.yview)

        self.attendancetable.heading("roll",text="RollNo")
        self.attendancetable.heading("name",text="Name")
        self.attendancetable.heading("department",text="Department")
        self.attendancetable.heading("time",text="Time")
        self.attendancetable.heading("date",text="Date")
        self.attendancetable.heading("attendance",text="AttendanceStatus")

        self.attendancetable["show"]="headings"
        self.attendancetable.column("roll",width=100)
        self.attendancetable.column("name",width=200)
        self.attendancetable.column("department",width=200)
        self.attendancetable.column("time",width=150)
        self.attendancetable.column("date",width=150)
        self.attendancetable.column("attendance",width=150)

        self.attendancetable.pack(fill=BOTH,expand=1)

        self.attendancetable.bind("<ButtonRelease>",self.get_cursor)

    def fetch_data(self,rows):
        self.attendancetable.delete(*self.attendancetable.get_children())
        for i in rows:
            self.attendancetable.insert("",END,values=i)
    
    # Import CSV
    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data()

    # Export CSV
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    # Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.attendancetable.focus()
        content=self.attendancetable.item(cursor_row)
        row=content['values']
        self.var_roll.set(row[0])
        self.var_name.set(row[1])
        self.var_dept.set(row[2])
        self.var_time.set(row[3])
        self.var_date.set(row[4])
        self.var_status.set(row[5])

    def reset_data(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dept.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_status.set("")



if __name__ == "__main__":
    root = Tk()
    obj = attendance(root)
    root.mainloop()