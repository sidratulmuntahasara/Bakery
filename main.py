##Import Modules
from tkinter.font import BOLD, ITALIC
import mysql.connector as myconn
import time
from tkinter import *
from PIL import Image, ImageTk
from employee import empClass
from product import prodClass
from create_order import orderClass
from tkinter import messagebox
from subprocess import call
import os
 
class BMS:
    def __init__(self,root):

        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Bakery Management System")
 
        #Title
        img1=Image.open("images/logo.png")
        img1_resize=img1.resize((80,80))
        self.icon_title=ImageTk.PhotoImage(img1_resize)
        title=Label(self.root, text="Bakery Management System", bd=0 , image = self.icon_title,  compound=LEFT, font=("times new roman",30,ITALIC), bg="#1A1A1A",fg="#E9E1F9", padx=40).place(x=0,y=0,relwidth=1,height=90)
 
        #Button_Logout
        btn_logout=Button(self.root, text="Logout", command=self.logout, font=("times new roman",15), bg="#D8D4C7", cursor="hand2", border=0, relief=RAISED, bd=5).place(x=1200,y=25,width=100,height=40)
       
        #Clock
        self.lbl_clock=Label(self.root, text="Welcome to Bakery Management System \t \t Date: DD-MM-YYYY \t \t Time: HH:MM:SS", bd=0, font=("times new roman",13), bg="#6F6F6F",fg="white")
        self.lbl_clock.place(x=0,y=90,relwidth=1,height=30)
 
        #Left Menu
        self.MenuLogo=Image.open("images/menulogo.png")
        self.MenuLogo_resize=self.MenuLogo.resize((200,200), Image.ANTIALIAS)
        self.MenuLogo_img=ImageTk.PhotoImage(self.MenuLogo_resize)
        leftMenu=Frame(self.root, bd=2, relief=RIDGE)
        leftMenu.place(x=0,y=120,width=250,height=566)
 
        lbl_menuLogo=Label(leftMenu, image=self.MenuLogo_img)
        lbl_menuLogo.pack(side=TOP, fill=X)
 
        # lbl_menu=Label(leftMenu).pack(side=TOP, fill=X)
 
        self.Home=Image.open("images/home.png")
        self.Home_resize=self.Home.resize((25,25), Image.ANTIALIAS)
        self.Home_img=ImageTk.PhotoImage(self.Home_resize)
        btn_dashboard=Button(leftMenu, text="HOME", image=self.Home_img, compound=LEFT, font=("times new roman",15,BOLD), bg="#23202A", fg="#F5EDDA", cursor="hand2", border=0, relief=RIDGE, bd=5, padx=8).pack(side=TOP, fill=X)
 
        lbl_menu=Label(leftMenu).pack(side=TOP, fill=X)
        lbl_menu=Label(leftMenu, text="Menu", font=("times new roman",15,BOLD), bg="#4B3B6C", fg="#D1C6EA").pack(side=TOP, fill=X)
 
       
        self.Arrow=Image.open("images/arrow.png")
        self.Arrow_resize=self.Arrow.resize((40,15), Image.ANTIALIAS)
        self.Arrow_img=ImageTk.PhotoImage(self.Arrow_resize)
        btn_dashboard=Button(leftMenu, text="Employee", command=self.employee, image=self.Arrow_img, compound=LEFT, anchor="w", font=("times new roman",15,ITALIC), bg="#E9E1F9", fg="#4B3B6C", cursor="hand2", border=0, relief=RAISED, bd=5, padx=10).pack(side=TOP, fill=X)
        btn_dashboard=Button(leftMenu, text="Products", command=self.product, image=self.Arrow_img, compound=LEFT, anchor="w", font=("times new roman",15,ITALIC), bg="#E9E1F9", fg="#4B3B6C", cursor="hand2", border=0, relief=RAISED, bd=5, padx=10).pack(side=TOP, fill=X)
        btn_dashboard=Button(leftMenu, text="Create a New Order", command=self.create_order, image=self.Arrow_img, compound=LEFT, anchor="w", font=("times new roman",15,ITALIC), bg="#E9E1F9", fg="#4B3B6C", cursor="hand2", border=0, relief=RAISED, bd=5, padx=10).pack(side=TOP, fill=X)
        # btn_dashboard=Button(leftMenu, text="Stock", image=self.Arrow_img, compound=LEFT, anchor="w", font=("times new roman",15,ITALIC), bg="#E9E1F9", fg="#4B3B6C", cursor="hand2", border=0, relief=RAISED, bd=5, padx=10).pack(side=TOP, fill=X)
        # btn_dashboard=Button(leftMenu, text="Customer Details", image=self.Arrow_img, compound=LEFT, anchor="w", font=("times new roman",15,ITALIC), bg="#E9E1F9", fg="#4B3B6C", cursor="hand2", border=0, relief=RAISED, bd=5, padx=10).pack(side=TOP, fill=X)
        btn_dashboard=Button(leftMenu, text="Exit", command=self.logout, image=self.Arrow_img, compound=LEFT, anchor="w", font=("times new roman",15,ITALIC), bg="#E9E1F9", fg="#4B3B6C", cursor="hand2", border=0, relief=RAISED, bd=5, padx=10).pack(side=TOP, fill=X)
       
 
        #Content
        self.lbl_Employee=Label(self.root, text="Employees", font=("goudy old style",18, ITALIC), bg="#4B3B6C", fg="#D1C6EA", relief=RIDGE, bd=3)
        self.lbl_Employee.place(x=350,y=170,width=250,height=50)
        self.lbl_Emp_no=Label(self.root, text="[ 0 ]", font=("goudy old style",18), fg="#4B3B6C", bg="#D1C6EA", relief=RIDGE, bd=3)
        self.lbl_Emp_no.place(x=350,y=220,width=250,height=50)
 
        self.lbl_Product=Label(self.root, text="Products", font=("goudy old style",18, ITALIC), bg="#4B3B6C", fg="#D1C6EA", relief=RIDGE, bd=3)
        self.lbl_Product.place(x=650,y=170,width=250,height=50)
        self.lbl_Prod_no=Label(self.root, text="[ 0 ]", font=("goudy old style",18), fg="#4B3B6C", bg="#D1C6EA", relief=RIDGE, bd=3)
        self.lbl_Prod_no.place(x=650,y=220,width=250,height=50)
 
        self.lbl_Sales=Label(self.root, text="Sales", font=("goudy old style",18, ITALIC), bg="#4B3B6C", fg="#D1C6EA", relief=RIDGE, bd=3)
        self.lbl_Sales.place(x=950,y=170,width=250,height=50)
        self.lbl_Sales=Label(self.root, text="[ 0 ]", font=("goudy old style",18), fg="#4B3B6C", bg="#D1C6EA", relief=RIDGE, bd=3)
        self.lbl_Sales.place(x=950,y=220,width=250,height=50)
       
        #footer
        lbl_footer=Label(self.root, text="Computer Project 2022-23 \t Developed by: Sidratul Muntaha Sara\t Class 12A\t\t", anchor="e", font=("candara",12, ITALIC), bg="#1A1A1A", fg="#E9E1F9").pack(side=BOTTOM, fill=X)

        self.update_content()

#===================================================================================================
#======================================= 2nd Window ===============================================
#===================================================================================================
 
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=empClass(self.new_win)
    
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=prodClass(self.new_win)

    def create_order(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=orderClass(self.new_win)

    def logout(self):
        res=messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if res==True:
            self.root.destroy()
            messagebox.showinfo("Logout", "You have successfully logged out")
            call(["python", "login.py"])
        else:
            pass

    def update_content(self):
        con=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
        cur=con.cursor()
        try:
            cur.execute("select * from employees")
            employee=cur.fetchall()
            self.lbl_Emp_no.config(text=f"[ {str(len(employee))} ]")

            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_Prod_no.config(text=f"[ {str(len(product))} ]")

            sales=self.count()
            self.lbl_Sales.config(text=f"[ {str(sales)} ]")

            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d/%m/%Y")
            self.lbl_clock.config(text=f"Welcome to Bakery Management System \t \t Date: {str(date_)} \t \t Time: {str(time_)}")
            self.lbl_clock.after(200, self.update_content)
        except Exception as ex:
            messagebox.showerror("Error",f"Due To: {str(ex)}",parent=self.root)

    def count(self):
        dir_path = r'./bills'
        count = 0
        for path in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, path)):
                count += 1
        return count
 
if __name__ == "__main__":
    root = Tk()
    obj=BMS(root)
    root.mainloop()
 
