from student import student
from studentpick import studentpick
from studentunpick import studentunpick
class Menu:
    def menuoptions(self):
        print("\tSTUDENT OPERATIONS")
        print("\t1. Studentpick")
        print("\t2. Studentunpick")
        print("\t3. Exit")
#mainprogram
Menu().menuoptions()
while True:
    ch=int(input("Enter your choice: "))
    match(ch):
        case 1:
            s1=studentpick()
            s1.studentdata()
        case 2:
            s2=studentunpick()
            s2.readdata()
        case 3:
            print("thanks for using")
            break
        case _:
            print("ue seleection is worg try again")
