from ctypes.wintypes import HPALETTE
import numpy as np
from heap import heap
import ctypes


class pqueue(heap):
    def __init__(self, htype='max'):
        super().__init__(htype)

    def pop(self):
        # dequeue
        if len(self._container) > 1:
            print(self._container)
            topPriority = self._container[1]

            self._container = self._container[1:]
            self._container[0] = 0
            self._length  = ctypes.c_int(self._container.shape[0]-1)
            self.build_heap()
            print("top priority is", topPriority)
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
    x = np.arange(9, dtype = np.int32)

    myqueue = pqueue()
    myqueue.read_data(x)
    myqueue.build_heap()
    myqueue.print_container()

    while True:
        priority = myqueue.pop()

        if priority is None:
            break

        print("done highest priority is", priority)

    myqueue.add(99)
    myqueue.add(1000)
    myqueue.add(50)





