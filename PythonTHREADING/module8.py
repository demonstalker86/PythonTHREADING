import time
import random
import threading
from threading import  current_thread


def test(barrier):
    # Python 3.10 - current_thread
    slp = random.randint(10,15)
    time.sleep(slp)
    print(f"Поток [{current_thread().name}] запущен в ({time.ctime()})")
    
    barrier.wait()
    print(f"Поток [{current_thread().name}] преодолел барьер в ({time.ctime()})")


bar = threading.Barrier(5)
for i in range(5): 
    threading.Thread(target=test, args=(bar,), name=f"thr-{i}").start()   