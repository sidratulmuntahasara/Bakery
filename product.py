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

class prodClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x520+250+150")
        self.root.title("Bakery Management System | Product Management")
        self.root.background=ImageTk.PhotoImage(file="images/bg.png")
        self.root.background_image=Label(self.root,image=self.root.background).place(x=0,y=0,relwidth=1,relheight=1)
        self.root.focus_force()

        #===================Variables===================
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_prod_id=StringVar()
        self.var_prod_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        
        
        #Title
        title=Label(self.root,text="Products Inventory",font=("candara",18,ITALIC, BOLD), fg="black", bg="#E5DEDB")
        title.place(x=0,y=20, relwidth=1,height=70)
 
        # txt_Search=Entry(self.root,text="Search",font=("times new roman",11),textvariable=self.var_searchtxt, bd=3,relief=GROOVE)
        # txt_Search.place(x=75,y=115,width=180, height=27)
 
        # btn_Search=Button(self.root,text="Search", command=self.search, font=("times new roman",11),bg="black",fg="white",cursor="hand2")
        # btn_Search.place(x=265,y=115,width=150)

        #Details
        lbl_Detail=Label(self.root, text="ENTER DETAILS",font=("Candara",15,BOLD), bg="#E9DDDD", fg="#2E2626")
        lbl_Detail.place(x=550,y=140,width=425,height=30)

        lbl_ProdID=Label(self.root, anchor="w",text="Product ID",font=("times new roman",12))
        lbl_ProdID.place(x=550,y=180,width=100,height=25)
 
        txt_ProdID=Entry(self.root,font=("times new roman",12),textvariable=self.var_prod_id ,bd=2,relief=GROOVE, bg="#372B2B", fg="white")
        txt_ProdID.place(x=675,y=180,width=300,height=25)
 
        lbl_Prod=Label(self.root, anchor="w",text="Product Name",font=("times new roman",12))
        lbl_Prod.place(x=550,y=220,width=100,height=25)
 
        txt_Prod=Entry(self.root,font=("times new roman",12),textvariable=self.var_prod_name,bd=2,relief=GROOVE, bg="#372B2B", fg="white")
        txt_Prod.place(x=675,y=220,width=300,height=25)

        lbl_Price=Label(self.root, anchor="w",text="Price",font=("times new roman",12))
        lbl_Price.place(x=550,y=260,width=100,height=25)
 
        txt_Price=Entry(self.root,font=("times new roman",12),textvariable=self.var_price ,bd=2,relief=GROOVE, bg="#372B2B", fg="white")
        txt_Price.place(x=675,y=260,width=300,height=25)
 
        lbl_Quantity=Label(self.root, anchor="w",text="Quantity",font=("times new roman",12))
        lbl_Quantity.place(x=550,y=300,width=100,height=25)
 
        txt_Quantity=Entry(self.root,font=("times new roman",12),textvariable=self.var_qty,bd=2,relief=GROOVE, bg="#372B2B", fg="white")
        txt_Quantity.place(x=675,y=300,width=300,height=25)


        #=================Buttons=================
        btn_Add=Button(self.root,text="Add",font=("times new roman",12), command=self.add_data, bg="#2196f3",fg="white",cursor="hand2")
        btn_Add.place(x=550,y=380,width=100,height=30)
        btn_Update=Button(self.root,text="Update",font=("times new roman",12), command=self.update_data,bg="#4caf50",fg="white",cursor="hand2")
        btn_Update.place(x=670,y=380,width=100,height=30)
        btn_Delete=Button(self.root,text="Delete",font=("times new roman",12), command=self.delete_data ,bg="#f44336",fg="white",cursor="hand2")
        btn_Delete.place(x=790,y=380,width=100,height=30)
        btn_Clear=Button(self.root,text="Clear",font=("times new roman",12), command=self.clear, bg="#607d8b",fg="white",cursor="hand2")
        btn_Clear.place(x=910,y=380,width=100,height=30)



        #=================Product Details Frame=================
        prod_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="black")
        prod_Frame.place(x=0,y=105,width=500,relheight=0.8)
 
        scroll_y=Scrollbar(prod_Frame,orient=VERTICAL)
        scroll_x=Scrollbar(prod_Frame,orient=HORIZONTAL)
        self.Product_Table=ttk.Treeview(prod_Frame,columns=("ProdID","Prod_Name","Price","Quantity"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Product_Table.xview)
        scroll_y.config(command=self.Product_Table.yview)
        self.Product_Table.heading("ProdID",text="ProdID")
        self.Product_Table.heading("Prod_Name",text="Prod_Name")
        self.Product_Table.heading("Price",text="Price")
        self.Product_Table.heading("Quantity",text="Quantity")
        self.Product_Table['show']='headings'
        self.Product_Table.column("ProdID",width=100)
        self.Product_Table.column("Prod_Name",width=100)
        self.Product_Table.column("Price",width=100)
        self.Product_Table.column("Quantity",width=100)
        self.Product_Table.pack(fill=BOTH,expand=1)
        self.Product_Table.bind("<ButtonRelease-1>",self.get_data)
 
        self.show()



        #=====================================================================================================
 
 
    def add_data(self): 
        con=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
        cur=con.cursor()
        try:
            if self.var_prod_id.get()=="":
                messagebox.showerror("Error","Product ID must be required",parent=self.root)
            else:
                cur.execute("Select * from product WHERE Prod_Id=%s",(self.var_prod_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product ID already exists",parent=self.root)
                else:
                    cur.execute("insert into product values(%s,%s,%s,%s)",(
                        self.var_prod_id.get(),
                        self.var_prod_name.get(),
                        self.var_price.get(),
                        self.var_qty.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product details has been added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Due To: {str(ex)}",parent=self.root)
 
    def show(self):
        con=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
        cur=con.cursor()
        self.Product_Table.delete(*self.Product_Table.get_children())
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.Product_Table.delete(*self.Product_Table.get_children())
            for row in rows:
                self.Product_Table.insert('',END,values=row)
        except Exception as es:
            messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)
 
 
    def fetch_data(self):
        con=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
        cur=con.cursor()
        cur.execute("select * from product")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Product_Table.delete(*self.Product_Table.get_children())
            for row in rows:
                self.Product_Table.insert('',END,values=row)
            con.commit()
        con.close()
 
    def get_data(self,ex):
        con=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
        cur=con.cursor()
        r=self.Product_Table.focus()
        content=(self.Product_Table.item(r))
        row=content['values']
        self.var_prod_id.set(row[0])
        self.var_prod_name.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
   
    def update_data(self):
        con=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
        cur=con.cursor()
        try:
            if self.var_prod_id.get()=="":
                messagebox.showerror("Error","Product ID must be required",parent=self.root)
            else:
                cur.execute("Select * from product where Prod_ID=%s",(self.var_prod_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product ID",parent=self.root)
                else:
                    cur.execute("update product set Prod_Name=%s,Price=%s,Quantity=%s where Prod_ID=%s",(
                        self.var_prod_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_prod_id.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Product Updated Successfully",parent=self.root)
                    self.show()
                    con.close()
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
 
    def delete_data(self):
        con=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
        cur=con.cursor()
        try:
            if self.var_prod_id.get()=="":
                messagebox.showerror("Error","Product ID must be required",parent=self.root)
            else:
                cur.execute("Select * from product where Prod_ID=%s",(self.var_prod_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Product ID",parent=self.root)
                else:
                    delete=messagebox.askyesno("Product Delete Page","Do you want to delete this Product",parent=self.root)
                    if delete==True:
                        cur.execute("delete from product where Prod_ID=%s",(self.var_prod_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Product Deleted Successfully",parent=self.root)
                        self.clear()
                    con.close()
        except Exception as es:
            messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
            
 
    def clear(self):
        self.var_prod_id.set("")
        self.var_prod_name.set("")
        self.var_price.set("")
        self.var_qty.set("")
        self.show()
        



    def search(self):
        con=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
        cur=con.cursor()
        self.Product_Table.delete(*self.Product_Table.get_children())
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select your option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search Input should be required",parent=self.root)

            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.Product_Table.delete(*self.Product_Table.get_children())
                    for row in rows:    
                        self.Product_Table.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)
        
        
        




if __name__ == "__main__":
    root = Tk()
    obj=prodClass(root)
    root.mainloop()
 
