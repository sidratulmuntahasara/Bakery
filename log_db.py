import mysql.connector as myconn
from subprocess import call


db=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
cur=db.cursor()

cur.execute("create table login(name varchar(30) not null,username varchar(100) not null primary key,password varchar(20) not null);")


#REMEMBER
# Username : admin
# Password : 12345
# this is default username and password for admin
cur.execute("insert into login values('ADMIN12345','admin','12345');")
db.commit()

call(["python", "login.py"])

