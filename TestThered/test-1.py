

import threading
import time

def worker(message):
    for i in range(5):
        print (message)
        time.sleep(1)
def work(message):
    for i in range(5):
        print (message)
        time.sleep(1)

nome = ''

t = threading.Thread(target=worker,args=("thread sendo executada",))
x = threading.Thread(target=work,args=("thread sendo executada",))
t.start()
x.start()
while t.isAlive() or x.isAlive():
    print ("Aguardando thread")
    time.sleep(5)

print ("Thread morreu")
print ("Finalizando programa")