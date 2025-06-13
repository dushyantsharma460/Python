# Ex :- import the github data of 100 user with the help of multithreading 
# If not using the multithreading we need to wait for all the process to complete

import threading
import time

def worker(num):
    print(f"Thread {num}: Starting")
    time.sleep(2)                                           # Simulate some work dealy of 2 sec
    print(f"Thread {num}: Finishing")


threads = []
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))       # make the tread for parllel execution
    threads.append(thread)                                   # append the making thread in list
    thread.start()

for thread in threads:
    thread.join()   
    
    # Wait for all threads to finish if not using join it will not wait for 2 sec it will execute other things
    
print("All threads completed.")


# Go and explore multi-process module it run process instead of thread