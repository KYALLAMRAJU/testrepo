from univ import univ
from collage import collage
class student(univ,collage):
    def getdata(self,name,number,marks):
         self.name=name
         self.number=number
         self.marks=marks
         print(self.name,self.number,self.marks)
         self.getunivdet()
         self.getcollagedet()
         self.displayuniv()
         self.displaycollage()
         self.displaystudent()
    def displaystudent(self):
        print("student name is : {}".format(self.name))
        print("location is : {}".format(self.number))
        print("marks is : {}".format(self.marks))
    # main program
s=student()
name=input("enter your name: ")
number=int(input("enter your number: "))
marks=int(input("enter your marks: "))
s.getdata(name,number,marks)

