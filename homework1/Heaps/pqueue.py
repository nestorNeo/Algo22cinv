from ctypes.wintypes import HPALETTE
import queue
import numpy as np
from heap import heap
import ctypes
import random
import time
import matplotlib.pyplot as plt


class pqueue(heap):
    def __init__(self, htype='max'):
        super().__init__(htype)

    def pop(self):
        # dequeue
        if len(self._container) > 1:
            #print(self._container)
            topPriority = self._container[1]

            self._container = self._container[1:]
            self._container[0] = 0
            self._length  = ctypes.c_int(self._container.shape[0]-1)
            self.build_heap()
            #print("top priority is", topPriority)
            return topPriority
        
        return None

    def add(self, element):
        # uglyness because numpy reference had to create a copy to enlarge the
        # array because the references sorry pal xD
        size = len(self._container)
        handler = self._container.copy()
        handler.resize( size + 1)
        handler[-1] = element
        self._container = handler
        self._length = ctypes.c_int(self._container.shape[0]-1)
        self.build_heap()
    
    
if __name__ == "__main__":
    x = np.arange(0, dtype = np.int32)

    myqueue = pqueue()
    myqueue.read_data(x)
    myqueue.build_heap()

    inputSize = range(1,10000)

    plotAdd = []
    plotpop = []
    plotMaxArraySizeX = []


    for n in inputSize:
        start = time.time()
        myqueue.add(random.randint(-10000,10000))
        end = time.time()
        plotMaxArraySizeX.append(n)
        plotAdd.append(end - start)

    while True:
        start = time.time()
        priority = myqueue.pop()
        end = time.time()
        if priority:
            plotpop.append(end - start)
        if priority is None:
            break

    fig, (ax,ay) = plt.subplots(2, 1)
    fig.subplots_adjust(hspace=0.5)
    ax.plot(plotMaxArraySizeX,plotAdd)
    ay.plot(plotpop)
    ay.invert_xaxis()
    
    
    ax.set_xlabel('Arreglo')
    ay.set_xlabel('Arreglo.')
    ay.set_ylabel('Tiempo elementos, sec')
    ax.grid(True)
    ay.grid(True)

    
    ax.set_ylabel('Entrada de elementos, sec')
    plt.savefig("grafy.jpg")






