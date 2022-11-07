from tkinter.font import BOLD, ITALIC
import mysql.connector as myconn
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import pymysql
import random
import os


 
db=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
cur=db.cursor()
 
 
class orderClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x520+250+150")
        self.root.title("Bakery Management System | Order")
        self.root.focus_force()
 
        #===================Variables===================
        self.var_bill_no=StringVar()
        self.var_bill_no.set(str(random.randint(1000,9999)))
        self.var_cust_name=StringVar()
        self.var_cust_phone=StringVar()
        self.var_item=StringVar()
        self.var_price=IntVar()
        self.var_qty=IntVar()
        self.var_total=StringVar()
        self.var_search_bill=StringVar()
        # self.var_gender=StringVar()
        # self.var_sal=StringVar()
        # self.var_job=StringVar()
        # self.var_dept=StringVar()
        global l
        l=[]

        #===================Functions===================
        def welcome():
            txtarea.delete(1.0,END)
            txtarea.insert(END,"\n\n\t\t Welcome to Bakery Management System")
            txtarea.insert(END,f"\n\n\t Today's Date: {datetime.now().date()}")
            txtarea.insert(END,f"\n\t Current Time: {datetime.now().time()}")
            txtarea.insert(END,f"\n\n\t Bill Number: {self.var_bill_no.get()}")
            txtarea.insert(END,f"\n\t Customer Name: {self.var_cust_name.get()}")
            txtarea.insert(END,f"\n\t Customer Phone: {self.var_cust_phone.get()}")
            txtarea.insert(END,f"\n\t ===========================================")
            txtarea.insert(END,f"\n\t Products\t\tQTY\t\tPrice")
            txtarea.insert(END,f"\n\t ===========================================\n")

        def additem():
            n=self.var_price.get()
            m=self.var_qty.get()*n
            l.append(m)
            if self.var_item.get()=="":
                messagebox.showerror("Error","Please Enter Product",parent=root)
            else:
                txtarea.insert(END,f"\n\t {self.var_item.get()}\t\t{self.var_qty.get()}\t\t{m}")

        def generate_bill():
            if self.var_cust_name.get()=="" or self.var_cust_phone.get()=="":
                messagebox.showerror("Error","Customer Details are must",parent=root)
            else:
                tex=txtarea.get(14.0,(14.0+float(len(l)+1)))
                welcome()
                txtarea.insert(END,tex)
                txtarea.insert(END,f"\n\t ===========================================")
                txtarea.insert(END,f"\n\t Total Bill Amount:\t\t\t{sum(l)}")
                txtarea.insert(END,f"\n\t ===========================================")
                txtarea.insert(END,f"\n\t Thanks for Shopping with us")
                txtarea.insert(END,f"\n\t Visit Again")
                txtarea.insert(END,f"\n\t ===========================================")
                savebill()

        def savebill():
            op=messagebox.askyesno("Save Bill","Do you want to save the Bill?",parent=root)
            if op>0:
                bill_data=txtarea.get('1.0',END)
                f1=open("bills/"+str(self.var_bill_no.get())+".txt","w")
                f1.write(bill_data)
                f1.close()
                messagebox.showinfo("Saved",f"Bill No.:{self.var_bill_no.get()} saved successfully",parent=root)
            else:
                return

        def clear():
            self.var_cust_name.set("")
            self.var_cust_phone.set("")
            self.var_item.set("")
            self.var_price.set(0)
            self.var_qty.set(0)
            self.var_total.set("")
            self.var_bill_no.set(str(random.randint(1000,9999)))
            welcome()

        def exit():
            op=messagebox.askyesno("Exit","Do you really want to exit?",parent=root)
            if op>0:
                root.destroy()
            



        #===================Title===================
        title=Label(self.root,text="Billing & Create Order",font=("candara",18,ITALIC, BOLD), fg="white", bg="#581845")
        title.pack(fill=X,ipady=7)

        #===================Customer details===================
        F1=LabelFrame(self.root,text="Customer Details",font=("candara",16,ITALIC, BOLD), fg="white", bg="#581845")
        F1.place(x=0,y=70,relwidth=1)

        lbl_cust_name=Label(F1,text="Customer Name",font=("candara",12,ITALIC, BOLD), fg="white", bg="#581845")
        lbl_cust_name.grid(row=0,column=0,padx=20,pady=5,sticky="w")

        txt_cust_name=Entry(F1,font=("candara",12,ITALIC, BOLD), fg="white", bg="#39122E",textvariable=self.var_cust_name)
        txt_cust_name.grid(row=0,column=1,padx=20,pady=5,sticky="w")

        lbl_cust_contact=Label(F1,text="Contact No.",font=("candara",12,ITALIC, BOLD), fg="white", bg="#581845")
        lbl_cust_contact.grid(row=0,column=2,padx=20,pady=5,sticky="w")

        txt_cust_contact=Entry(F1,font=("candara",12,ITALIC, BOLD), fg="white", bg="#39122E", textvariable=self.var_cust_phone)
        txt_cust_contact.grid(row=0,column=3,padx=20,pady=5,sticky="w")


        #===================Input Product===================
        F2=LabelFrame(self.root,text="Order Here",font=("candara",16,ITALIC, BOLD), fg="white", bg="#581845")
        F2.place(x=5,y=150,width=500,height=365)

        item=Label(F2,text="Product Name",font=("candara",13,ITALIC, BOLD), fg="white", bg="#581845")
        item.grid(row=0,column=0,padx=30,pady=20,sticky="w")
        item_txt=Entry(F2,width=20,font=("candara",13,ITALIC, BOLD), fg="white", bg="#39122E", textvariable=self.var_item)
        item_txt.grid(row=0,column=1,padx=10,pady=20,sticky="w")

        price=Label(F2,text="Product Price",font=("candara",13,ITALIC, BOLD), fg="white", bg="#581845")
        price.grid(row=1,column=0,padx=30,pady=10,sticky="w")
        price_txt=Entry(F2,width=20,font=("candara",13,ITALIC, BOLD), fg="white", bg="#39122E", textvariable=self.var_price)
        price_txt.grid(row=1,column=1,padx=10,pady=10,sticky="w")

        quantity=Label(F2,text="Product Quantity",font=("candara",13,ITALIC, BOLD), fg="white", bg="#581845")
        quantity.grid(row=2,column=0,padx=30,pady=20,sticky="w")
        quantity_txt=Entry(F2,width=20,font=("candara",13,ITALIC, BOLD), fg="white", bg="#39122E", textvariable=self.var_qty)
        quantity_txt.grid(row=2,column=1,padx=10,pady=20,sticky="w")


        #===================Button===================
        btn_Add=Button(self.root,text="Add Item",command=additem, font=("times new roman",13), bg="#2196f3",fg="white",cursor="hand2")
        btn_Add.place(x=70,y=380,width=110,height=35)
        btn_Generate=Button(self.root,text="Generate Bill", command=generate_bill, font=("times new roman",13), bg="#4caf50",fg="white",cursor="hand2")
        btn_Generate.place(x=70,y=430,width=110,height=35)
        btn_Clear=Button(self.root,text="Clear", command=clear, font=("times new roman",13), bg="#f44336",fg="white",cursor="hand2")
        btn_Clear.place(x=200,y=380,width=110,height=35)
        btn_Exit=Button(self.root,text="Exit", command=exit, font=("times new roman",13), bg="#607d8b",fg="white",cursor="hand2")
        btn_Exit.place(x=200,y=430,width=110,height=35)


        #===================Billing Area===================
        F3=Frame(root,relief=GROOVE,bd=10)
        F3.place(x=530,y=150,width=550,height=360)

        bill_title=Label(F3,text="Bill Area",font=("candara",15,ITALIC, BOLD), relief=GROOVE,bd=7).pack(fill=X)
        scroll_y=Scrollbar(F3,orient=VERTICAL)
        txtarea=Text(F3,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=txtarea.yview)
        txtarea.pack()
        welcome()


if __name__ == "__main__":
    root = Tk()
    obj=orderClass(root)
    root.mainloop()