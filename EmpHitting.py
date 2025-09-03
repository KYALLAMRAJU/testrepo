import sys,time,gc
from EmpDev import *
from EmpRaising import *
print("-"*50)
print("EMPLOYEE OPERATIONS")
print("-"*50)
db=dbprogram()
print("is gc enabled ?",gc.isenabled())
print("content of object at first creation:",db.__dict__)
def empmenu():
    print("\t1.Check connection")
    print("\t2.Table existance")
    print("\t3.CREATE TABLE")
    print("\t4.MANIPULATE DATA")
    print("\t5.RETRIEVE DATA")
    print("\t6.EXIT")
print("-"*50)
while(True):
    empmenu()
    ch = int(input("Enter your choice: "))
    if (ch < 0):
        print("Enter a valid choice")
    else:
        match(ch):
            case 1:
                try:
                   db.connection()
                except ConnectionError:
                    print("Check the credentials- try again")
                except Exception as e1:
                    print("OOPS something went wrong try again:", e1)
            case 2:
                try:
                    tablename = input("Enter Table Name: ")
                    db.tablecheck(tablename)
                except TableAlreadyExists:
                    print("Table already exists- not possible to create again Create with a new name")
            case 3:
                try:
                    db.create()
                except pyodbc.ProgrammingError as e:
                    print(e)
                except pyodbc.IntegrityError as e:
                    print(e)
                except pyodbc.DatabaseError as e:
                    print(e)
            case 4:
                try:
                    db.insert()
                except pyodbc.IntegrityError as e:
                    print(e)
                except pyodbc.DatabaseError as e:
                    print(e)
            case 5:
                try:
                    db.retrieve()
                except pyodbc.ProgrammingError as e:
                    print(e)
            case 6:
                print("Thank You- PROGRAM EXECUTION COMPLETED")
                del db
                gc.disable()
                print("is gc running now ?", gc.isenabled())
                gc.collect()  # force garbage collection
                exit()



