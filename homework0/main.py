import numpy as np 
from numpy.ctypeslib import ndpointer 
import ctypes
from ctypes import c_int
import pathlib

class Node(ctypes.Structure):
    _fields_ = [("next", ctypes.c_void_p), ("value", ctypes.c_int)]

if __name__ == "__main__":
    libname = pathlib.Path().absolute() / "liblistx.so"
    c_lib = ctypes.CDLL(libname)

    # Define return void pointer
    c_lib.show_list.restype = ctypes.c_void_p
    c_lib.show_list.argtypes = [ctypes.c_void_p]

    A = Node(0, 10)
    B = Node(0, 20)
    C = Node(0, 30)

    A.next = ctypes.addressof(B)
    B.next = ctypes.addressof(C)

    c_lib.show_list(ctypes.byref(A))
    # Define arguments
