from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue
import os
import queue
from sys import ps1
import time

def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1

if __name__ == "__main__":

    q = Queue()
    
    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=m)

