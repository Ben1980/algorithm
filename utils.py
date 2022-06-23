import time
import random

def MeasureExecutionTime(f, unsortedList):
    duration = 0.0
    for i in range(1000):
        start = time.time()
        f(unsortedList)
        end = time.time()
        duration += end-start
    
    return duration/1000

def RandomList(size):
    list = []
    for i in range(size):
        list.append(random.randint(-100,100))

    return list
