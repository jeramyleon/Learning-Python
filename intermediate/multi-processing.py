from multiprocessing import Process, Value, Array, Lock
from multiprocessing import Queue
from multiprocessing import Pool
import os
import queue
import time

def cube(number):
    return number*number*number

if __name__ == "__main__":

    numbers = range(10)
    pool = Pool()

    # map, apply, join, close 
    result = pool.map(cube, numbers)
    # pool.apply(cube, numbers[0])

    pool.close()
    pool.join()

    print(result)

