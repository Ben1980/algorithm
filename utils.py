import time
import random
import copy
from inspect import signature

class Measure(object):
    name = ''
    duration = 0
    input = []
    output = []
    benchmark = False
    numIt = 100
    listSize = 1000
    rangeFrom = -100
    rangeTo = 100

    def __init__(self, benchmark) -> None:
        self.benchmark = benchmark

    def Name(self, name):
        self.name = name
        return self

    def __RandomList(self):
        size = self.listSize if self.benchmark else 8
        list = [random.randint(self.rangeFrom, self.rangeTo) for i in range(size)]

        return list

    def MeasureExecutionTime(self, f):
        if self.benchmark:
            self.__Benchmark(f)
        else:
            input = self.__RandomList()
            self.input = copy.deepcopy(input)
            f(input)
            self.output = input

        return self

    def Results(self):
        if self.benchmark:
            return [self.name, self.duration]
        
        return [self.name, self.input, self.output]

    def __Benchmark(self, f):
        d = 0.0
        for i in range(self.numIt):
            inputList = self.__RandomList()
            start = time.time()
            f(inputList)
            end = time.time()
            d += end-start

        self.duration = d/self.numIt

    def NumberOfIterations(self, numIt):
        self.numIt = numIt
        return self
    
    def ListSize(self, size):
        self.listSize = size
        return self
    
    def Range(self, rangeFrom, ragneTo):
        self.rangeFrom = rangeFrom
        self.rangeTo = ragneTo
        return self

def TableHeader(benchmarkMode):
    if benchmarkMode:
        return ['Algorithm', 'Duration']
    return ['Algorithm', 'Input', 'Output']

