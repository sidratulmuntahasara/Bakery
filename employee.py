#Import Modules
from tkinter.font import BOLD, ITALIC
import mysql.connector as myconn
from datetime import datetime
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import pymysql
 

db=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
cur=db.cursor()
 
 
class empClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x520+250+150")
        self.root.title("Bakery Management System | Employee")
        self.root.focus_force()
 
        #===================Variables===================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_emp_id=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_contact=StringVar()
        self.txt_Address=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_gender=StringVar()
        self.var_sal=StringVar()
        self.var_job=StringVar()
        self.var_dept=StringVar()

 
        #SearchFrame
        searchFrame=LabelFrame(self.root,text="Search Employee",font=("candara",15, ITALIC, BOLD), fg="black",bd=2,relief=RIDGE)
        searchFrame.place(x=250,y=20,width=600,height=70)
 
        #Options
        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby ,font=("times new roman",11),state="readonly",justify=CENTER)
        cmb_search['values']=("Select","Employee ID","Name","Contact", "Email")
        cmb_search.current(0)
        cmb_search.place(x=15,y=10,width=180)
 
        txt_Search=Entry(searchFrame,font=("times new roman",11),textvariable=self.var_searchtxt, bd=2,relief=GROOVE)
        txt_Search.place(x=215,y=10,width=180, height=25)
 
        btn_Search=Button(searchFrame,text="Search", command=self.search, font=("times new roman",11),bg="black",fg="white",cursor="hand2")
        btn_Search.place(x=415,y=7,width=150)
 
        #Title
        title=Label(self.root,text="Employee Details",font=("candara",18,ITALIC, BOLD), fg="white", bg="#282828")
        title.place(x=0,y=105,width=1100,height=40)
 
        #Details
        lbl_EmpID=Label(self.root, anchor="w",text="Employee ID",font=("times new roman",12),bg="#F0F0F0")
        lbl_EmpID.place(x=50,y=165,width=100,height=25)
 
        txt_EmpID=Entry(self.root,font=("times new roman",12),textvariable=self.var_emp_id ,bd=2,relief=GROOVE)
        txt_EmpID.place(x=150,y=165,width=200,height=25)
 
        lbl_Name=Label(self.root, anchor="w",text="Name",font=("times new roman",12),bg="#F0F0F0")
        lbl_Name.place(x=50,y=205,width=100,height=25)
 
        txt_Name=Entry(self.root,font=("times new roman",12),textvariable=self.var_name,bd=2,relief=GROOVE)
        txt_Name.place(x=150,y=205,width=200,height=25)
 
        lbl_Contact=Label(self.root, anchor="w",text="Contact",font=("times new roman",12),bg="#F0F0F0")
        lbl_Contact.place(x=50,y=245,width=100,height=25)
 
        txt_Contact=Entry(self.root,font=("times new roman",12),textvariable=self.var_contact,bd=2,relief=GROOVE)
        txt_Contact.place(x=150,y=245,width=200,height=25)
 
        lbl_Address=Label(self.root, anchor="w",text="Address",font=("times new roman",12),bg="#F0F0F0")
        lbl_Address.place(x=50,y=285,width=100,height=25)
 
        self.txt_Address=Text(self.root,font=("times new roman",12),bd=2,relief=GROOVE)
        self.txt_Address.place(x=150,y=285,width=200,height=70)
 
        lbl_DOB=Label(self.root, anchor="w",text="Date of Birth",font=("times new roman",12),bg="#F0F0F0")
        lbl_DOB.place(x=400,y=165,width=100,height=25)
 
        txt_DOB=DateEntry(self.root,selectmode="day",font=("Arial",10), date_pattern="yyyy/mm/dd",textvariable=self.var_dob,bd=2,relief=GROOVE)
        txt_DOB.place(x=500,y=165,width=200,height=25)
 
        lbl_Gender=Label(self.root, anchor="w",text="Gender", font=("times new roman",12),bg="#F0F0F0")
        lbl_Gender.place(x=400,y=205,width=100,height=25)
        cmb_Gender=ttk.Combobox(self.root,font=("times new roman",11),textvariable=self.var_gender,state="readonly",justify=LEFT)
        cmb_Gender['values']=( "Select","Male","Female","Other")
        cmb_Gender.current(0)
        cmb_Gender.place(x=500,y=205,width=200,height=25)
 
        lbl_Email=Label(self.root, anchor="w",text="Email",font=("times new roman",12),bg="#F0F0F0")
        lbl_Email.place(x=400,y=245,width=100,height=25)
 
        txt_Email=Entry(self.root,font=("times new roman",12),textvariable=self.var_email,bd=2,relief=GROOVE)
        txt_Email.place(x=500,y=245,width=200,height=25)
 
        lbl_DOJ=Label(self.root, anchor="w",text="Date of Joining",font=("times new roman",12),bg="#F0F0F0")
        lbl_DOJ.place(x=400,y=285,width=100,height=25)
 
        txt_DOJ=DateEntry(self.root,selectmode="day", date_pattern="yyyy/mm/dd" ,font=("Arial",10),textvariable=self.var_doj,bd=2,relief=GROOVE)
        txt_DOJ.place(x=500,y=285,width=200,height=25)
 
        lbl_Salary=Label(self.root, anchor="w",text="Salary",font=("times new roman",12),bg="#F0F0F0")
        lbl_Salary.place(x=400,y=325,width=100,height=25)
 
        txt_Salary=Entry(self.root,font=("times new roman",12),textvariable=self.var_sal,bd=2,relief=GROOVE)
        txt_Salary.place(x=500,y=325,width=200,height=25)
 
        lbl_Job=Label(self.root, anchor="w",text="Job Title",font=("times new roman",12),bg="#F0F0F0")
        lbl_Job.place(x=750,y=165,width=100,height=25)
 
        txt_Job=Entry(self.root,font=("times new roman",12),textvariable=self.var_job,bd=2,relief=GROOVE)
        txt_Job.place(x=850,y=165,width=200,height=25)
 
        lbl_Dept=Label(self.root, anchor="w",text="Department",font=("times new roman",12),bg="#F0F0F0")
        lbl_Dept.place(x=750,y=205,width=100,height=25)
        cmb_Dept=ttk.Combobox(self.root,font=("times new roman",11),textvariable=self.var_dept,state="readonly",justify=LEFT)
        cmb_Dept['values']=( "Select","HR","Sales","IT","Finance","Admin")
        cmb_Dept.current(0)
        cmb_Dept.place(x=850,y=205,width=200,height=25)
 
 
        #=================Buttons=================
        btn_Add=Button(self.root,text="Add",font=("times new roman",12), command=self.add_data, bg="#2196f3",fg="white",cursor="hand2")
        btn_Add.place(x=750,y=260,width=100,height=30)
        btn_Update=Button(self.root,text="Update",font=("times new roman",12), command=self.update_data,bg="#4caf50",fg="white",cursor="hand2")
        btn_Update.place(x=750,y=300,width=100,height=30)
        btn_Delete=Button(self.root,text="Delete",font=("times new roman",12), command=self.delete_data ,bg="#f44336",fg="white",cursor="hand2")
        btn_Delete.place(x=875,y=260,width=100,height=30)
        btn_Clear=Button(self.root,text="Clear",font=("times new roman",12), command=self.clear, bg="#607d8b",fg="white",cursor="hand2")
        btn_Clear.place(x=875,y=300,width=100,height=30)
 
 
        #=================Employee Details Frame=================
        emp_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        emp_Frame.place(x=0,y=380,relwidth=1,height=150)
 
        scroll_y=Scrollbar(emp_Frame,orient=VERTICAL)
        scroll_x=Scrollbar(emp_Frame,orient=HORIZONTAL)
        self.Employee_Table=ttk.Treeview(emp_Frame,columns=("EmpID","Name","Contact","Address","DOB","Gender","Email","DOJ","Salary","Job","Department"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Employee_Table.xview)
        scroll_y.config(command=self.Employee_Table.yview)
        self.Employee_Table.heading("EmpID",text="EmpID")
        self.Employee_Table.heading("Name",text="Name")
        self.Employee_Table.heading("Contact",text="Contact")
        self.Employee_Table.heading("Address",text="Address")
        self.Employee_Table.heading("DOB",text="DOB")
        self.Employee_Table.heading("Gender",text="Gender")
        self.Employee_Table.heading("Email",text="Email")
        self.Employee_Table.heading("DOJ",text="DOJ")
        self.Employee_Table.heading("Salary",text="Salary")
        self.Employee_Table.heading("Job",text="Job")
        self.Employee_Table.heading("Department",text="Department")
        self.Employee_Table['show']='headings'
        self.Employee_Table.column("EmpID",width=100)
        self.Employee_Table.column("Name",width=100)
        self.Employee_Table.column("Contact",width=100)
        self.Employee_Table.column("Address",width=100)
        self.Employee_Table.column("DOB",width=100)
        self.Employee_Table.column("Gender",width=100)
        self.Employee_Table.column("Email",width=100)
        self.Employee_Table.column("DOJ",width=100)
        self.Employee_Table.column("Salary",width=100)
        self.Employee_Table.column("Job",width=100)
        self.Employee_Table.column("Department",width=100)
        self.Employee_Table.pack(fill=BOTH,expand=1)
        self.Employee_Table.bind("<ButtonRelease-1>",self.get_data)
 
        self.show()
        # self.Employee_Table.bind("<ButtonRelease-1>",self.get_data)
        # self.fetch_data()
 
 
#=====================================================================================================
 
 
    def add_data(self): 
        con=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employees WHERE EmpId=%s",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Employee ID already exists",parent=self.root)
                else:
                    cur.execute("insert into employees values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_Address.get('1.0',END),
                        self.var_dob.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_doj.get(),
                        self.var_sal.get(),
                        self.var_job.get(),
                        self.var_dept.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee details has been added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Due To: {str(ex)}",parent=self.root)
 
    def show(self):
        con=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
        cur=con.cursor()
        self.Employee_Table.delete(*self.Employee_Table.get_children())
        try:
            cur.execute("select * from employees")
            rows=cur.fetchall()
            self.Employee_Table.delete(*self.Employee_Table.get_children())
            for row in rows:
                self.Employee_Table.insert('',END,values=row)
        except Exception as es:
            messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)
 
 
    def fetch_data(self):
        con=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
        cur=con.cursor()
        cur.execute("select * from employees")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Employee_Table.delete(*self.Employee_Table.get_children())
            for row in rows:
                self.Employee_Table.insert('',END,values=row)
            con.commit()
        con.close()
 
    def get_data(self,ev):
        con=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
        cur=con.cursor()
        r=self.Employee_Table.focus()
        content=(self.Employee_Table.item(r))
        row=content['values']
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_Address.delete('1.0',END)
        self.txt_Address.insert(END,row[3])
        self.var_dob.set(row[4])
        self.var_gender.set(row[5])
        self.var_email.set(row[6])
        self.var_doj.set(row[7])
        self.var_sal.set(row[8])
        self.var_job.set(row[9])
        self.var_dept.set(row[10])
   
    def update_data(self):
        con=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employees where EmpID=%s",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    cur.execute("update employees set Name=%s,Contact=%s,Address=%s,DOB=%s,Gender=%s,Email=%s,DOJ=%s,Salary=%s,Job=%s,Dept=%s where EmpID=%s",(
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_Address.get('1.0',END),
                        self.var_dob.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_doj.get(),
                        self.var_sal.get(),
                        self.var_job.get(),
                        self.var_dept.get(),
                        self.var_emp_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Employee Updated Successfully",parent=self.root)
                    self.show()
                    con.close()
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
 
    def delete_data(self):
        con=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","Employee ID must be required",parent=self.root)
            else:
                cur.execute("Select * from employees where EmpID=%s",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID",parent=self.root)
                else:
                    delete=messagebox.askyesno("Employee Delete Page","Do you want to delete this employee",parent=self.root)
                    if delete==True:
                        cur.execute("delete from employees where EmpID=%s",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Employee Deleted Successfully",parent=self.root)
                        self.clear()
                    con.close()
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            
 
    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_Address.delete('1.0',END)
        self.var_dob.set("")
        self.var_gender.set("")
        self.var_email.set("")
        self.var_doj.set("")
        self.var_job.set("")
        self.var_dept.set("")
        self.show()


    def search(self):
        con=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
        cur=con.cursor()
        self.Employee_Table.delete(*self.Employee_Table.get_children())
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select your option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search Input should be required",parent=self.root)

            else:
                cur.execute("select * from employees where "+str(self.var_searchby.get())+" LIKE '%+str(self.var_searchtxt.get())+%'")
                # cur.execute("select * from employees where "+self.var_searchby.get()+" LIKE '% "+self.var_searchtxt.get()+" %'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.Employee_Table.delete(*self.Employee_Table.get_children())
                    for row in rows:    
                        self.Employee_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)
 

 
if __name__ == "__main__":
    root = Tk()
    obj=empClass(root)
    root.mainloop()