import raiseexc
import devexc
import importlib,time
while(True):
    try:
        n=int(input("Enter a number: "))
        res=raiseexc.table(n)
        time.sleep(10)
        print("reloading raiseexc ...")
        importlib.reload(raiseexc)
        n = int(input("Enter a number: "))
        res=raiseexc.table(n)
    except devexc.zeroerror as e:
        print(e)
    except devexc.negativenumber as e:
        print(e)
    except:
        print("oops something went wrong")
    else:
        print("thanks for using program")
        break