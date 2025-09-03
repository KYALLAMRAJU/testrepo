import types
from logging import exception
class student:
    def readstudentdata(self,objinfo): #instance method
        #print("id of {} in instance method after calling :".format(self),id(self))
        print("enter the {} student details :".format(objinfo))
        self.sno=int(input("enter {} student number:".format(objinfo)))
        self.sname=input("enter {} student name:".format(objinfo))
        self.smarks=input("enter {}student marks:".format(objinfo))
        self.readstudentoutput(objinfo)
    @classmethod
    def studentaddress(cls):
        student.city="HYD"
        student.state="NY"
        student.country="USA"
        student.phone="555-555-5555"
        student.email="<abcd@gmail.com>"
    def readstudentoutput(self, objinfo):
        print("res of {} STUDENT is".format(objinfo))
        student.studentaddress()
        for k, v in {**self.__dict__, **self.__class__.__dict__}.items():
            if not k.startswith("__") and not callable(v) and not isinstance(v, (
            classmethod, staticmethod, types.FunctionType)):
                pass
class teacher:
    def teacherdetails(self,objinfo):
        print("enter the {} student details :".format(objinfo))
        self.tno = int(input("enter {} teacher number:".format(objinfo)))
        self.tname = input("enter {} teacher name:".format(objinfo))
        self.trole = input("enter {}teacher role:".format(objinfo))
class school:
    def schooldetails(self, objinfo):
        print("enter the {} student details :".format(objinfo))
        self.scno = int(input("enter {} school number:".format(objinfo)))
        self.scname = input("enter {} school name:".format(objinfo))
        self.scrole = input("enter {}school role:".format(objinfo))
        self.smarks=input("enter {}student marks:".format(objinfo))
class display:
    @staticmethod
    def showdata(obj,objinfo):
        print("="*50)
        print("{} information".format(objinfo))
        print("=" * 50)
        for k, v in {**obj.__dict__, **obj.__class__.__dict__}.items():
            if not k.startswith("__") and not callable(v) and not isinstance(v, (
            classmethod, staticmethod, types.FunctionType)):
                print("{}...>{}".format(k, v))
        print("=" * 50)
#mainprogram
s=student()   #creating an object of respective classes
t=teacher()
sc=school()
s.readstudentdata("registered") #calling the funcitons of respective classes
t.teacherdetails("registered")
sc.schooldetails("registered")
display().showdata(s,"student") #displaying data using static method w.r.t class name
display().showdata(t,"teacher")
display().showdata(sc,"school")

class fact:
    def getval(self):
        while(True):
            try:
                self.n = int(input("Enter the number to calculate the factorial details: "))
            except Exception as e:
                print(e)
            else:
                break
    def calfact(self):
        if(self.n<0):
            print("{} is not a positive number".format(self.n))
        else:
            fact=1
            i=1
            while(i<=self.n):
               fact=fact*i
               i=i+1
            return fact
    def displayfact(self):
        self.getval()
        self.calfact()
        print("the fact of {} is {}".format(self.n,self.calfact()))
#mainprogram
fact().displayfact()


class const:
    def __init__(self,a=1,b=2,c=3):
        self.a=a
        self.b=b
        self.c=c
        print("the value of {} and {} and {}".format(a,b,c))
    #main
c1=const()
c2=const(10,20,30)


class c1:
    def disp1(self):
        print("c1 --disp1()")
class c2:
    def disp2(self):
        print("c2 --disp2()")
class c3(c2,c1):
    def disp3(self):
        print("c3 --disp3()")
#main
o1=c1()
o2=c2()
o3=c3()
o1.disp1()
o2.disp2()
o3.disp3()

class c1:
    def disp1(self):
        print("c1 --disp1()")
class c2:
    def disp2(self):
        print("c2 --disp2()")
class c3(c2,c1):
    def disp3(self):
        print("c3 --disp3()")
#main
o3=c3()
o3.disp1()
o3.disp2()
o3.disp3()

class c1:
    def disp1(self):
        print("c1 --disp1()")
class c2:
    def disp2(self):
        print("c2 --disp2()")
class c3(c1,c2):
    def disp3(self):
        self.disp1()
        self.disp2()
        print("c3 --disp3()")
#main
o3=c3()
o3.disp3()


class c1:
    def getA(self):
        self.a=10
        print("value of a is {}".format(self.a))
class c2:
    def getB(self):
        self.b=20
        print("value of b is {}".format(self.b))
class c3(c1,c2):
    def getC(self):
        self.c=30
    def data(self):
        self.d=self.a+self.b+self.c
        print("value of d is {}".format(self.d))
#mainprogram
o3=c3()
print(o3.__dict__)
o3.getA()
print(o3.__dict__)
o3.getB()
print(o3.__dict__)
o3.getC()
print(o3.__dict__)
o3.data()



class c1:
    def getA(self):
        self.a=10
class c2:
    def getB(self):
        self.b=20
class c3(c1,c2):
    def getC(self):
        self.c=30
    def data(self):
        self.getA()
        self.getB()
        self.getC()
        self.d=self.a+self.b+self.c
        print("value of d is {}".format(self.d))
#mainprogram
o3=c3()
o3.data()


class c1:
    def get(self):
        print("this is first class method output")
class c2:
    def get(self):
        print("this is second class method output")
class c3(c2,c1):
    def get(self):
        print("this is third class method output")
        super().get()
        c2.get(self)
#main
o3=c3()
o3.get()

class c1:
    def get(self):
        print("this is first class method output")
class c2:
    def get(self):
        print("this is second class method output")
class c3(c2,c1):
    def get(self):
        print("this is third class method output")
        c1.get(self)
        c2.get(self)
#main
o3=c3()
o3.get()


class c1:
    def __init__(self):
        print("this is default method output")
class c2(c1):
    def __init__(self):
        print("this is c2 method output")
        super().__init__()
#main
o2=c2()


