import threading,time
class hyd:
    def squares(self,lst):
        for val in lst:
            print("({})={}".format(val,val**2))
            time.sleep(0.5)
    def cubes(self,lst):
        for val in lst:
            print("({})={}".format(val,val**3))
            time.sleep(0.5)
#main
h=hyd()
print("program execution started by: {}".format(threading.current_thread().name))
print("="*50)
st=time.time()
lst=[2,6,8,10,11,22,50]
t1=threading.Thread(target=h.squares,args=(lst,))
t1.name="sqthread"
print("status of t1 before start()=",t1.is_alive())
print("="*50)
t2=threading.Thread(target=h.cubes,args=(lst,))
t2.name="cubethread"
print("status of t2 before start()=",t2.is_alive())
print("="*50)
print("number of active threads before start()=",threading.active_count())
t1.start()
t2.start()
print("="*50)
print("status of t1 after start()=",t1.is_alive())
print("status of t2 after start()=",t2.is_alive())
print("number of active threads after start()=",threading.active_count())
t1.join()
t2.join()
et=time.time()
print("total time to complete the program using threading is :{}".format(et-st))
print("="*50)
print("program execution ended by: {}".format(threading.current_thread().name))
print("="*50)
print("number of active threads after program completion=",threading.active_count())

import threading,time
class numbers:
    def __init__(self,num):
        self.num=num
    def gen(self):
        if self.num < 0:
            print("entered value is less than zero- input a valid number again")
        else:
            print("="*50)
            print("number of values within {} is:".format(self.num))
            for i in range(0,self.num):
                print("{}...>{}".format(threading.current_thread().name,i))
                time.sleep(0.5)
            print("="*50)
#main
threading.Thread(target=numbers(int(input("enter num:"))).gen).start()

import threading,time
class evenodd:
    def even(self,n):
        if(n<=0):
            print("entered value is less than zero- input a valid number again")
            print("current thread:".format(threading.current_thread().name))
        else:
            for i in range(2,n+1,2):
                print("{}...>{}".format(threading.current_thread().name,i))
                time.sleep(0.5)
    def odd(self,n):
        if(n<=0):
            print("entered value is less than zero- input a valid number again")
            print("current thread:".format(threading.current_thread().name))
        else:
            for i in range(1,n+1,2):
                print("{}...>{}".format(threading.current_thread().name,i))
                time.sleep(0.5)
#main
eo=evenodd()
t1=threading.Thread(target=eo.odd,args=(int(input("enter num:")),))
t2=threading.Thread(target=eo.even,args=(int(input("enter num:")),))
t1.start()
t2.start()


import threading,time
class evenodd:
    def even(self,lst):
            for i in lst:
                if i % 2 == 0:
                    print("{}...>{}".format(threading.current_thread().name,i))
                    time.sleep(0.5)
    def odd(self,lst):
            for i in lst:
                if i % 2 == 1:
                    print("{}...>{}".format(threading.current_thread().name,i))
                    time.sleep(0.5)
#main
lst=[1,22,55,23,40,25,899,900,458,5623,55889,20,3]
eo=evenodd()
print("program execution started by: {}".format(threading.current_thread().name))
t1=threading.Thread(target=eo.odd,args=(lst,))
t1.name="oddthread"
t2=threading.Thread(target=eo.even,args=(lst,))
t2.name="eventhread"
t1.start()
t2.start()
t1.join()
t2.join()
print("program execution ended by: {}".format(threading.current_thread().name))

import threading,time
def mul(n):
    l.acquire()
    if(n<=0):
        print("entered value is less than zero- input a valid number again")
    else:
        print("mul table for : {}".format(threading.current_thread().name),n)
        for i in range(1,11):
            print("{}...>{}*{}={}".format(threading.current_thread().name,n,i,n*i))
            time.sleep(0.5)
        print("="*50)
    l.release()
#main
l=threading.Lock()
t1=threading.Thread(target=mul,args=(int(input("enter num:")),))
t2=threading.Thread(target=mul,args=(int(input("enter num:")),))
t1.start()
t2.start()


import threading,time
class multable:
    @classmethod
    def getlock(cls):
        cls.l=threading.Lock()
    def mul(n):
        csl.l.acquire()
        l.acquire()
        if(n<=0):
            print("entered value is less than zero- input a valid number again")
        else:
            print("mul table for : {}".format(threading.current_thread().name),n)
            for i in range(1,11):
                print("{}...>{}*{}={}".format(threading.current_thread().name,n,i,n*i))
                time.sleep(0.5)
            print("="*50)
        multable.l.release()
#main
multable.getlock()
t1=threading.Thread(target=mul,args=(int(input("enter num:")),))
t2=threading.Thread(target=mul,args=(int(input("enter num:")),))
t1.start()
t2.start()


import threading,time
def moviereservation(nos):
    l.acquire()
    global totalseats
    if(nos>totalseats):
        print("\t Hi {} selected seats {} are not available- select fewer seats".format(threading.current_thread().name,nos))
    else:
        totalseats-=nos
        print("\t Hi {} {} seats selected continue for chewckput".format(threading.current_thread().name,nos))
        time.sleep(0.5)
        print("\t now available seats are {}".format(totalseats))
        time.sleep(2)
        if(totalseats==0):
            print("seats are full try next show")
    l.release()
#main
totalseats=10
l=threading.Lock()
#subtrhreads
t1=threading.Thread(target=moviereservation,args=(int(input("select no of seats:")),))
t1.name="kalyan"
t2=threading.Thread(target=moviereservation,args=(int(input("select no of seats:")),))
t2.name="sammy"
t3=threading.Thread(target=moviereservation,args=(int(input("select no of seats:")),))
t3.name="mia"
t4=threading.Thread(target=moviereservation,args=(int(input("select no of seats:")),))
t4.name="blacky"
t5=threading.Thread(target=moviereservation,args=(int(input("select no of seats:")),))
t5.name="donald"
t6=threading.Thread(target=moviereservation,args=(int(input("select no of seats:")),))
t6.name="mark"
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()


import threading,time
def moviereservation(nos):
    l.acquire()
    global totalseats
    if(nos>totalseats):
        print("\t Hi {} selected seats {} are not available- select fewer seats".format(threading.current_thread().name,nos))
    else:
        totalseats-=nos
        print("\t Hi {} {} seats selected continue for chewckput".format(threading.current_thread().name,nos))
        time.sleep(0.5)
        print("\t now available seats are {}".format(totalseats))
        time.sleep(2)
        if(totalseats==0):
            print("seats are full try next show")
    l.release()
#main
totalseats=10
l=threading.Lock()
#subtrhreads
t1=threading.Thread(target=moviereservation,args=(int(input("select no of seats:")),))
t1.name="kalyan"
t2=threading.Thread(target=moviereservation,args=(int(input("select no of seats:")),))
t2.name="sammy"
t3=threading.Thread(target=moviereservation,args=(int(input("select no of seats:")),))
t3.name="mia"
t4=threading.Thread(target=moviereservation,args=(int(input("select no of seats:")),))
t4.name="blacky"
t5=threading.Thread(target=moviereservation,args=(int(input("select no of seats:")),))
t5.name="donald"
t6=threading.Thread(target=moviereservation,args=(int(input("select no of seats:")),))
t6.name="mark"
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()




import threading,time
class oopsthread:
    @classmethod
    def getlock(cls):
        cls.l=threading.Lock()
        cls.totalseats=10
    def __init__(self,nos):
        self.nos=nos
    def moviereservation(self):
        oopsthread.l.acquire()
        if(self.nos>oopsthread.totalseats):
            print("\t Hi {} selected seats {} are not available- select fewer seats".format(threading.current_thread().name,self.nos))
        else:
            oopsthread.totalseats-=self.nos
            print("\t Hi {} {} seats selected continue for chewckput".format(threading.current_thread().name,self.nos))
            time.sleep(0.5)
            print("\t now available seats are {}".format(oopsthread.totalseats))
            time.sleep(2)
            if(oopsthread.totalseats==0):
                print("seats are full try next show")
        oopsthread.l.release()
#main
#subtrhreads
oopsthread.getlock()
t1=threading.Thread(target=oopsthread(2).moviereservation)
t1.name="kalyan"
t2=threading.Thread(target=oopsthread(2).moviereservation)
t2.name="sammy"
t3=threading.Thread(target=oopsthread(2).moviereservation)
t3.name="mia"
t4=threading.Thread(target=oopsthread(2).moviereservation)
t4.name="blacky"
t5=threading.Thread(target=oopsthread(2).moviereservation)
t5.name="donald"
t6=threading.Thread(target=oopsthread(2).moviereservation)
t6.name="mark"
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()


















