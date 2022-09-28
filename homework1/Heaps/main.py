from cgi import test
import numpy as np 
from heap import heap


def startHeap(x, htype="max"):
    HObject = heap(htype)
    HObject.read_data(x)
    HObject.print_container()
    HObject.build_heap()
    HObject.print_container()
    print(HObject._length)


if __name__ == "__main__":

    # Object heap
    

    inputSize = range(10,13)

    for n in inputSize:
        print("value of n", n)
        x = np.arange(n, dtype = np.int32 )
        startHeap(x)

    for n in inputSize:
        print("value of n", n)
        x =np.arange(n, 0, -1, dtype = np.int32 )
        startHeap(x, htype="min")