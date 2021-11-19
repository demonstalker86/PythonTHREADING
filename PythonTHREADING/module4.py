import time
import threading


#value = 0
locker = threading.RLock()

#def inc_value():
#    global value
#    while True:
#        with locker:
#            value += 1        
#            print(value)
#            time.sleep(0.1)
            

#for _ in range(5):
#    threading.Thread(target=inc_value).start()

def inc_value():
    print("Блокируем поток..")
    locker.acquire()
    print("Поток разблокирован..")


t1 = threading.Thread(target=inc_value)
t2 = threading.Thread(target=inc_value)
t1.start()
t2.start()