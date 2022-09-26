# -*- coding: utf-8 -*-
#!/usr/bin/env python
import numpy as np 
from numpy.ctypeslib import ndpointer 
import ctypes
from ctypes import POINTER, ARRAY, c_float, c_int 
import pathlib

if __name__ == "__main__":

    tlabel = 1

    if tlabel == 1:
        # Load the shared library into c types.
        libname = pathlib.Path().absolute() / "LibrarySort.so"

        c_lib = ctypes.CDLL(libname)

        # Define return void pointer
        c_lib.LibrarySort.restype = ctypes.c_void_p

        singlepp = ndpointer(dtype = np.int32, ndim = 1, flags = 'C') 

        c_lib.LibrarySort.argtypes = [singlepp, ctypes.c_int]

        x = np.arange(9, 0, -1 , dtype = np.int32 )

        print(x)

        m = ctypes.c_int(x.shape[0]) 
       
        c_lib.LibrarySort(x, m)

        print(x)


        

