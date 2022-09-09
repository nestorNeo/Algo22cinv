import numpy as np 
from numpy.ctypeslib import ndpointer 
import ctypes
from ctypes import c_int 
import pathlib

if __name__ == "__main__":

    
    libname = pathlib.Path().absolute() / "liblistx.so"
    c_lib = ctypes.CDLL(libname)
