from cgi import test
import numpy as np 
from heap import heap
import matplotlib.pyplot as plt
import time

def startHeap(x, htype="max"):
    HObject = heap(htype)
    HObject.read_data(x)
    #HObject.print_container()
    HObject.build_heap()
    #HObject.print_container()
    #print(HObject._length)

if __name__ == "__main__":
    # Object heap
    inputSize = range(10,200000)

    plotMaxArraySizeX = []
    plotMaxExecution  = []
    plotMinExecution =  []
      
    for n in inputSize:
        print("value of n", n)
        x = np.arange(n, dtype = np.int32 )
        start = time.time()
        startHeap(x)
        end = time.time()
        plotMaxArraySizeX.append(n)
        plotMaxExecution.append(end - start)

    for n in inputSize:
        print("value of n", n)
        x =np.arange(n, 0, -1, dtype = np.int32 )
        start = time.time()
        startHeap(x, htype="min")
        end = time.time()
        plotMinExecution.append(end - start)


    fig, (ax,ay) = plt.subplots(2, 1)
    fig.subplots_adjust(hspace=0.5)
    ax.plot(plotMaxArraySizeX,plotMaxExecution)
    ay.plot(plotMaxArraySizeX,plotMinExecution)
    
    ax.set_xlabel('Arreglo')
    ax.set_ylabel('Tiempo')
    ay.set_xlabel('Arreglo')
    ay.set_ylabel('Tiempo')
    ax.grid(True)
    ay.grid(True)

    
    ax.set_ylabel('Tiempo')
    plt.savefig("graficas.jpg")
