from ctypes import CDLL
import ctypes

if __name__ == "__main__":
   test = CDLL("./sum.so").Test
   test.restype = ctypes.c_int64
   print(test())