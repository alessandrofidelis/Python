from threading import *
import time
import random

def proca():
    semaa.acquire()
    time.sleep(random.randint(1,3))
    print("is ",end="")
    time.sleep(random.randint(1,3))
    print("La ",end="")
    time.sleep(random.randint(1,3))
    semab.release()
        
def procb():
    time.sleep(random.randint(1,3))
    print("Sou ",end="")
    time.sleep(random.randint(1,3))
    semac.release()
    semab.acquire()
    print("Sal",end="")
    time.sleep(random.randint(1,3))
    semac.release()

def procc():
    semac.acquire()
    time.sleep(random.randint(1,3))
    print("ma",end="")
    time.sleep(random.randint(1,3))
    semaa.release()
    semac.acquire()
    print("le ",end="")
    time.sleep(random.randint(1,3))    
    
semaa = Lock()
semab = Lock()
semac = Lock()
    
semaa.acquire()
semab.acquire()
semac.acquire()
    
threads = []
threads.append(Thread(target=proca))
threads.append(Thread(target=procb))
threads.append(Thread(target=procc))
for i in range(3):
    
	threads[i].start()

for i in range(3):
    threads[i].join()
    

print()    