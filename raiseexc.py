from devexc import zeroerror,negativenumber
msg1="diviision by 0 is not allowed"
msg2="don't enter below 0 values always enter above 0 only"
def table(n):
    if(n<0):
        raise zeroerror(msg1)
    elif(n==0):
        raise negativenumber(msg2)
    else:
        print("the entered number is {}".format(n))
        for j in range(1,11):
            print("{}*{}={}".format(n,j,n*j))


