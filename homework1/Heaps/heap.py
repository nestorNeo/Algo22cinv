import ctypes
from numpy.ctypeslib import ndpointer 
import numpy as np
import pathlib
import sys
import os

class heap:
    
    
    def __init__(self, htype = 'max'):

        # Load the shared library into c types.
        self._bsize = 9
        self._heap_name =  pathlib.Path(os.environ.get("HEAPLIB")).absolute()/"testheap.so"

        if not self._heap_name:
            raise "missing c implementation please set HEAPLIB otherwise die"

        self._singlepp = ndpointer(dtype = np.int32, ndim = 1, flags = 'C')
        self._cheap = ctypes.CDLL(self._heap_name)
        self._cheap.max_heapify.argtypes = [self._singlepp, ctypes.c_int, ctypes.c_int]
        self._cheap.max_heapify.restype = ctypes.c_void_p
        self._cheap.min_heapify.argtypes = [self._singlepp, ctypes.c_int, ctypes.c_int]
        self._cheap.min_heapify.restype = ctypes.c_void_p
        self._cheap.build_max_heap.argtypes = [self._singlepp, ctypes.c_int]
        self._cheap.build_max_heap.restype = ctypes.c_void_p
        self._cheap.build_min_heap.argtypes = [self._singlepp, ctypes.c_int]
        self._cheap.build_min_heap.restype = ctypes.c_void_p
        # Container and variables for the heap
        self._container = np.zeros(self._bsize, dtype = np.int32) # We use a eight size int 64 
        self._length  = ctypes.c_int(self._bsize) 
        self._hsize = ctypes.c_int(0)
        # Set heap type
        self._theap = htype

    def heapify(self, i):
   
        # Stop executuion if somebody has changed the type
        if not isinstance(self._container, np.ndarray) or not (self._container.dtype == 'int32'):
            raise TypeError('_container is not ndarray of int32')

        # Selecting the correct heap
        if self._theap == "max":
            self._cheap.max_heapify(self._container, ctypes.c_int(i), self._hsize)
        else:
            self._cheap.min_heapify(self._container, ctypes.c_int(i), self._hsize)

    def read_data(self, arr):
        """
        Reading and converting array
        """
        if not isinstance(arr, np.ndarray) or not (arr.dtype == 'int32'):
            raise TypeError('_container is not ndarray of int 32')
        
        # Set the heap container
        self._container = np.hstack([np.zeros(1, dtype = np.int32), arr]) 

        self._length  = ctypes.c_int(arr.shape[0]) 
        self._hsize = ctypes.c_int(arr.shape[0])
        
    def print_container(self):
        """
        Printing container
        """
        for i in range(1, len(self._container)):
            print(str(self._container[i]), end=' ')
        print('')

    def build_heap(self):
        """
        Build heap
        """
        # Selecting the correct heap
        if self._theap == "max":
            self._cheap.build_max_heap(self._container, self._length)
        else:
            self._cheap.build_min_heap(self._container, self._length)


