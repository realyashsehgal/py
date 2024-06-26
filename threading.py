import threading # type: ignore
import time
def eating():
    time.sleep(3)
    print("i am done eating")
def drinking():
    time.sleep(4)
    print("yo i am done drinking")
def study():
    time.sleep(6)
    print('yoo done study nvm it can never happen')
print("Threads")
x = threading.Thread(target=eating,args=())
x.start()
y = threading.Thread(target=drinking,args=())
y.start()
z = threading.Thread(target=study,args=())
z.start()
print(threading.active_count())
print(threading.enumerate())
#so here in this program all the threads are working simultaneously 
#we can use x.join() to make the other threads wait for that one to complete
