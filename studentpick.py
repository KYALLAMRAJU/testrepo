import pickle
from student import student
class studentpick:
    def studentdata(self):
        while(True):
            with open("studentrecord1.data","ab") as fp:
                name=int(input("enter the student number: "))
                number=input("enter the student name:")
                marks=int(input("enter the student age:"))
                s=student(name,number,marks)
                pickle.dump(s,fp)
                ch=input("do you want to enter another record ?: ")
                if(ch.lower()=="n"):
                    break
        print("student record saved in the file")

