from sys import getsizeof
from EmpDev import *
import pyodbc
totalmemoryspace=0

class dbprogram:
    def __init__(self):
        self.drivername = "SQL Server"
        self.server = "."
        self.database = "INDIAN_BANK"
        self.username = "sa"
        self.password = "123456789"
#to calculate the size
        self.size=getsizeof(self)
        global totalmemoryspace
        totalmemoryspace += self.size
        print("Total Memory Space: ",totalmemoryspace)

    def connection(self):
        try:
            ping = pyodbc.connect(
                f"DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={self.server};DATABASE={self.database};"
                f"UID={self.username};PWD={self.password};TrustServerCertificate=yes")
            print("Connection successful")
            #print(type(ping), ping)
            cur = ping.cursor()
            #print("cursor created",type(cur))
            return ping,cur
        except:
            raise ConnectionError
    def tablecheck(self,tablename):
        ping, cur = self.connection()
        cur.execute("SELECT * FROM SYS.TABLES WHERE NAME='{}'".format(tablename))
        res=cur.fetchall()
        if res:
            print("Table found",res[0][0])
            return res[0][0]
        else:
            return None
    def create(self):
        try:
            ping,cur=self.connection()
            tablename = input("Enter Table Name: ")
            if self.tablecheck(tablename):
                print("Table {} cannot be created already exsists".format(tablename))
                return tablename
            else:
                Columns=int(input("enter how many columns and conditions you want to create :"))
                col=[]
                for val in range(Columns):
                    colnames=input("enter Column {} Name and type (eg. INT,NOT NULL,VARCHAR,...ETC):".format(val+1))
                    col.append(colnames)
                print(col)
                print("All the column names entered- Now create table")
                SQL=("create table {} ({})").format(tablename,",".join(col))
                table=cur.execute(SQL)
                ping.commit()
                print("Table created successfully")
                return tablename,col
        except:
            raise TableAlreadyExists
    def insert(self):
        try:
            ping, cur = self.connection()
            tablename = input("Enter Table Name: ")
            res = self.tablecheck(tablename)
            if not res:
                print("Table {} does not exsist please create new table using create".format(tablename))
                tablename, col=self.create()
            elif (res == tablename):
                cur.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{tablename}'")
                col_names = [row[0] for row in cur.fetchall()]
                print("Detected columns:", col_names)
                rows=[]
                while True:
                    data=[]
                    for name in col_names:
                        val=input("enter data for{} : ".format(name))
                        data.append(val)
                    rows.append(tuple(data))
                    nextrow=input("enter next row(y/n): ").lower()
                    if nextrow == "n":
                        break
                    print(data)
                print(rows)
                placeholders = ",".join(["?"] * len(col_names))
                sql=f"insert into {tablename} ({','.join(col_names)}) VALUES({placeholders})"
                cur.execute(sql,rows)
                ping.commit()
                print("records inserted successfully")
        except:
            raise WrongInputError
    @staticmethod
    def retrieve():
        try:
            db=dbprogram()
            ping,cur=db.connection()
            tablename = input("Enter Table Name: ")
            res =db.tablecheck(tablename)
            if not res:
                print("Table {} does not exsist please create new table using create".format(tablename))
                tablename, col=db.create()
            else:
                sql=f"select * from {tablename}"
                cur.execute(sql)
                metadata=cur.description
                for col in metadata:
                    print(col[0],end="\t")
                print()
                records=cur.fetchall()
                print("=" * 50)
                for rows in records:
                    for val in rows:
                        print(val,end="\t")
                    print()
                print("=" * 50)
        except WrongInputError:
            raise WrongInputError

    def __del__(self):
        print("garbage collection called for de-allocating memory space")
        global totalmemoryspace
        totalmemoryspce=totalmemoryspace-self.size
        print("Now the total memory space after the deallocation is = {}".format(totalmemoryspce))















