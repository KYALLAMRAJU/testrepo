from atmdev import *
from devexc import negativenumber,zeroerror
bal=10000
pin=2815
msg1="enter amount more than 0 Rs"
msg2="0 amount withdraw not possible"

def verifypin():
    attempts=0
    maxattempts=3
    while(attempts<maxattempts):
     try:
        enteredpin=int(input("enter pin number:"))
        if (enteredpin == pin):
            print("Pin verified-now you can continue with Atm operations")
            return True
        else:
            attempts = attempts + 1
            print("invalid-pin {} attempts left".format(maxattempts-1))
     except ValueError as e:
         print(e)
         attempts+=1
    print("too many attempts cancelling the transaction")
    return False

def deposit():
    global bal
    deposit=int(input("Enter the deposit amount:"))
    if(deposit<0):
        raise negativenumber(msg1)
    if(deposit==0):
        raise invaliddeposit
    else:
        bal=bal+deposit
        print("balance amount after deposit is:{}".format(bal))

def withdraw():
    global bal
    withdraw=int(input("Enter the withdraw amount:"))
    if(withdraw<0):
        raise negativenumber(msg1)
    elif(withdraw==0):
        raise zeroerror(msg2)
    elif(withdraw>bal):
        raise balancelimitexceeded
    else:
        bal=bal-withdraw
        print("balance amount after withdrawl is:{}".format(bal))

def balancecheck():
    global bal
    print("your available balance is :{}".format(bal))

import pickle
def savecustomerdata(name):
    global bal
    with open(name,"ab") as fp:
        while(True):
            customerno=int(input("enter customer no:"))
            customername=input("enter customer name:")
            customeraddress=input("enter customer address:")
            customerbal=bal
            lst=[]
            lst.append(str(customerno)+"\t")
            lst.append(customername+"\t")
            lst.append(customeraddress+"\t\t")
            lst.append(str(customerbal)+"\t")
            pickle.dump(lst,fp)
            print("customer data saved successfully")
            ch=input("do you want to exit?(y/n)")
            if(ch.lower()=="y"):
                print("Thanks for using")
                break

import pickle
def readsavedcustomerdata(name):
    with open(name,"rb") as fp:
        while (True):
            data=pickle.load(fp)
            for val in data:
                print("{}".format(val),end=" ")
            print()


def genexample(start=0,stop=0,step=1):
    if((start==stop) and (stop==step)):
        raise InvalidInputGiven
    else:
        if(start>=stop):
            stop=start
            start=0
    while(start<stop):
        yield start
        start+=step
