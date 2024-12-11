def success():
    while True:
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")
        print("***************************************************MAIN MENU******************************************************")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")
        print("1.Add Record")
        print("2.Display Record")
        print("3.Search Record")
        print("4.Delete Record")
        print("5.Update Record")
        print("6.Exit")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")
#add record
        a=int(input("enter your choice="))
        if(a==1):
            print("-------------------------------------------------------------------------------------------------------------------------------------------------")
            print("****************************************ENTER DETAILS OF STUDENT******************************************")
            print("***************************************************MAIN MENU******************************************************")
            R=input("Enter Rollno:")
            N=input("Enter Name:")
            F=input("Enter Class:")
            D=input("Enter Fee=")
            mycursor=mydatabase.cursor()
            sql="Insert into students (Rollno,Name,Class,Fee) values(%s,%s,%s,%)"
            valu=(R,N,F,D)
            mycursor.execute(sql,valu)
            mydatabase.commit()
            print("\t\t\t\tInformation Saved")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------")
#dispaly all information
        elif(a==2):
            mycursor=mydatabase.cursor()
            mycursor.execute("select *from students")
            myresult=mycursor.fetchall()
            t=PrettyTable(['Rollno','Name','Class','Fees'])
            for Rollno,Name,cls,fee, in myresult:
                t.add_row([Rollno,Name,cls,fee])
            print(t)
#search student by Rollno
        elif(a==3):
            print("-------------------------------------------------------------------------------------------------------------------------------------------------")
            print("**************************************SEARCH STUDENT BY ROLLNO******************************************")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------")
            r_1=input("Enter student Rollno:")
            mycursor=mydatabase.cursor()
            mycursor.execute("select * from students where rollno="+r_1)
            myresult=mycursor.fetchall()
            t=PrettyTable(['Rollno','Name','Class','Fees'])
            for Rollno,Name,cls,fee in myresult:
                t.add_row([Rollno,Name,cls,fee])
            print(t)
#delete student information by Rollno
        elif(a==4):
            print("-------------------------------------------------------------------------------------------------------------------------------------------------")
            print("***************************************DELETE RECORD BY ROLLNO*******************************************")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------")
            r_1=input("Enter student Rollno whoes Information you want to Delete=")
            mycursor=mydatabase.cursor()
            mycursor.execute("delete from students where Rollno="+r_1)
            mydatabase.commit()
            print("\t\t\t\tRecord Deleted Successfully !!!")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------")
#update student fees Information By Rollno
        elif(a==5):
            r_1=input("Enter Rollno whoes fees you want to update=")
            Newfees=input("Enter New Fees:")
            mycursor=mydatabase.cursor()
            mycursor.execute("Update students set Fee="+Newfees+' where Rollno='+r_1+';')
            mydatabase.commit()
            mycursor.execute("select * from students where Rollno="+str(r_1))
            myresult=mycursor.fetchall()
            t=PrettyTable(['Rollno','Name','Class','Fee'])
            for Rollno,Name,cls,fee in myresult:
                t.add_row([Rollno,Name,cls,fee])
            print(t)
#exit
        else:
            exit()
#main section
from prettytable import PrettyTable
import mysql.connector
mydatabase=mysql.connector.connect(host="localhost",user="root",password="rishav")
#here mydatabase in connection object
'''CREATING DATABASE & TABLE'''
mycursor=mydatabase.cursor()#----------cursor is used to row row by processing of record in resultset
                                                    #----------mycursor is cursor object
mycursor.execute("create database if not exists studentrecord")
mycursor.execute("use studentrecord")
mycursor.execute("create table if not exists students(Rollno integer,Name varchar(20),class varchar(5),Fee integer)")
while True:
    print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    print("*******************************************************LOGIN********************************************************")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    
    username=input("Enter Username :")
    password=input("Enter Password :")
    if username=="nmlkps" and password=="1234":
        print("\t\t\t\t LOGIN SUCCESSFULL")
        success()
    else:
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\t\t\t\tINVALID USERNAME OR PASSWORD !!!!!!")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")
        break
    

    

        

