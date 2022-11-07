import mysql.connector as myconn
 
mydb=myconn.connect(host="localhost",user="root",password="12345",database="bakeryms")
mycursor=mydb.cursor()