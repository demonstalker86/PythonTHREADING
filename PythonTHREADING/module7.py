import time
import random
from threading import Thread, BoundedSemaphore, current_thread


max_connections = 5
pool = BoundedSemaphore(value=max_connections)


def test():
    with pool:
        # Python 3.10 - current_thread
        slp = random.randint(1,5)
        print(f"{current_thread().name} - sleep ({slp})")
        time.sleep(slp)

for i in range(10): 
    threading.Thread(target=test, name=f"thr-{i}").start()            