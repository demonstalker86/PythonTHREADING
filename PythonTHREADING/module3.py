import time
import threading

#def get_data(data, value):
#    for _ in range(value):
#        print(f"[{threading.currentThread().name}] - {data}")
#        time.sleep(1)

def get_data(data):
   for _ in range(5):
        # Python3.10
        print(f"[{threading.current_thread().name}] - {data}")
        # Python3.9
        #print(f"[{threading.currentThread().name}] - {data}")
        time.sleep(1)


thr = threading.Thread(target=get_data, args=(str(time.time()),), daemon=True)
# Python3.9
#thr.setDaemon(True)
# Python3.10
thr.daemon = True
thr.start()
time.sleep(1)
print("finish")


#thr_list = []


#for i in range(3):
#    thr = threading.Thread(target=get_data, args=(str(time.time()), i,), name=f"thr-{i}")
#    thr_list.append(thr)
#    thr.start()

#for i in thr_list:
#    i.join()



#print("name:", threading.main_thread().name)
#threading.main_thread().setName("result")
#print("result:", threading.main_thread().name)

#for i in range(100):
#    print(F"current: {i}")
#    time.sleep(1)

#    if i % 10 == 0:
#        print("active thread:", threading.active_count())
#        print("enumerate:", threading.enumerate())
#        print("thr-1 is alive:", thr.is_alive())