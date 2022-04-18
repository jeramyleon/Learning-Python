from multiprocessing import Process
import os
import time 
from threading import Thread

def square_numbers():
    for i in range(100):
        i * i 
        time.sleep(0.1)

threads = []
num_threads = 10

# create threads
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# start 
for t in threads:
    t.start 

# join
for t in threads:
    t.join()

print('end main')

