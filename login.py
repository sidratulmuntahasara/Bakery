from tkinter.font import BOLD, ITALIC
import mysql.connector as myconn
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from subprocess import call
import os

#REMEMBER
# Username : admin
# Password : 12345
# this is default username and password for admin

def log():
    
    db=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
    cur=db.cursor()
    username=f1.get()
    password=f2.get()

    sql="select * from login where username=%s and password=%s"
    cur.execute(sql,[(username),(password)])
    result=cur.fetchall()
    if result:
        messagebox.showinfo("Success","Login Successful")
        root.destroy()
        call(["python", "main.py"])
        return True

    else:
        messagebox.showerror("Error","Invalid Username or Password")        
        return False
        

root=Tk()
root.title("Login")
root.config(bg="#1A1A1A")
root.geometry("1350x700+0+0")
global f1,f2

Label(root, text="Admin Login", font=('Candara',18,BOLD,ITALIC), bg='#1A1A1A', fg='white', anchor=CENTER).pack(pady=200, fill=X)
Label(root, text="Username", font=('Candara',12), bg='#1A1A1A', fg='white',).place(x=525,y=300)
Label(root, text="Password", font=('Candara',12), bg='#1A1A1A', fg='white',).place(x=525,y=350)

f1=Entry(root, width=30, font=('Candara',12))
f1.place(x=630,y=300)
f2=Entry(root,show="*", width=30, font=('Candara',12))
f2.place(x=630,y=350)
f2.config(show="*")


Button(root, text="Login", command=log, height=2, width=10, cursor="hand2").place(x=650,y=430)

root.mainloop()