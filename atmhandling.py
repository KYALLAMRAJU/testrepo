from atmraising import *
from atmdev import *
if verifypin():pass
else:
    exit()

def menu():
    print("\t ATM OPERATIONS")
    print("\t1.DEPOSIT")
    print("\t2.WITHDRAW")
    print("\t3.AVAILABLE BALANCE")
    print("\t4.Save Data")
    print("\t5.Read Data")
    print("\t6.EXIT")
while(True):
    menu()
    ch=int(input("Enter your choice: "))
    if(ch<0):
        print("Enter a valid choice")
    else:
        match(ch):
            case 1:
                try:
                    deposit()
                except negativenumber as e:
                    print(e)
                except invaliddeposit:
                    print("deposit should be greater than 0 value")
                except Exception as e1:
                    print("OOPS something went wrong try again:",e1)
            case 2:
                try:
                    withdraw()
                except negativenumber as e:
                    print(e)
                except zeroerror as e:
                    print(e)
                except balancelimitexceeded:
                    print("withdraw amount should not be greater than balance amount")
                except BaseException as e2:
                    print("OOPS something went wrong try again:",e2)
            case 3:
                try:
                    balancecheck()
                except Exception as e3:
                    print("OOPS something went wrong try again:",e3)
            case 4:
                try:
                    name = input("enter the name the name of the file you want to load the data and read data from:")
                    savecustomerdata(name)
                except filealreadythere:
                    print("File already exists try with a different name")
                except BaseException as e4:
                    print("OOPS something went wrong try again:",e4)
            case 5:
                try:
                    name = input("enter the name the name of the file you want to load the data and read data from:")
                    readsavedcustomerdata(name)
                except filenothere:
                    print("File does not exist-check name again")
                except filecomplete:
                    print("reached end of the file")
                    break
                except BaseException as e5:
                    print("OOPS something went wrong try again:",e5)

            case 6:
                print("thank you for using my program")
                exit()
            case _:
                print("invalid input")



