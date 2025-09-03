import threading
tname=threading.current_thread().name
print("default thread name is: {}".format(tname))
noth=threading.active_count()
print("number of active threads:{}".format(noth))

import threading,time
def squares(lst):
    for val in lst:
        print("{}....>({})={}".format(threading.current_thread().name,val,val**2))
        time.sleep(0.5)
def cubes(lst):
    for val in lst:
        print("{}....>({})={}".format(threading.current_thread().name,val,val**3))
        time.sleep(0.5)
#main program
st=time.time()
lst=[0,2,6,8,10,11,22,50]
squares(lst)
print("="*50)
cubes(lst)
print("="*50)
et=time.time()
print("total time to complete the program using single thread is :{}".format(et-st))
noth=threading.active_count()
print("number of active threads:{}".format(noth))

import threading,time
def squares(lst):
    for val in lst:
        print("{}....>({})={}".format(threading.current_thread().name,val,val**2))
        time.sleep(0.5)
def cubes(lst):
    for val in lst:
        print("{}....>({})={}".format(threading.current_thread().name,val,val**3))
        time.sleep(0.5)
#main program
st=time.time()
lst=[0,2,6,8,10,11,22,50]
t1=threading.Thread(target=squares,args=(lst,))
print("="*50)
t2=threading.Thread(target=cubes,args=(lst,))
print("="*50)
#dispatch the subthreads
t1.start()
t2.start()
t1.join()
t2.join()
et=time.time()
print("total time to complete the program using threading is :{}".format(et-st))

import threading
def welcome(name1):
    print("{}......>Hi {}, good evening \n".format(threading.current_thread().name,name1))
#main
print("program execution started by {}".format(threading.current_thread().name))
t1=threading.Thread(target=welcome,args=("kalyan",))
t1.name="testname"
t1.start()
print("program execution ended by {}".format(threading.current_thread().name))


 #total thread functoions
import threading,time
def squares(lst):
    for val in lst:
        print("({})={}".format(val,val**2))
        time.sleep(0.5)
def cubes(lst):
    for val in lst:
        print("({})={}".format(val,val**3))
        time.sleep(0.5)
#main
print("program execution started by: {}".format(threading.current_thread().name))
print("="*50)
st=time.time()
lst=[2,6,8,10,11,22,50]
t1=threading.Thread(target=squares,args=(lst,))
t1.name="sqthread"
print("status of t1 before start()=",t1.is_alive())
print("="*50)
t2=threading.Thread(target=cubes,args=(lst,))
t2.name="cubethread"
print("status of t2 before start()=",t2.is_alive())
print("="*50)
print("number of active threads before start()=",threading.active_count())
t1.start()
t2.start()
print("status of t1 after start()=",t1.is_alive())
print("status of t2 after start()=",t2.is_alive())
print("number of active threads after start()=",threading.active_count())
print("="*50)
t1.join()
t2.join()
et=time.time()
print("total time to complete the program using threading is :{}".format(et-st))
print("="*50)
print("program execution ended by: {}".format(threading.current_thread().name))
print("="*50)
print("number of active threads after program completion=",threading.active_count())



























