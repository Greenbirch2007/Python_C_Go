

#
from ctypes import CDLL
import ctypes
#
# if __name__ == "__main__":
#    test = CDLL("./sum.so").Test
#    test.restype = ctypes.c_int64
#    print(test())


sum = CDLL("./sum.so").Sum
sum.argtypes = [ctypes.c_int32, ctypes.c_int32]
sum.restype = ctypes.c_int32
print(sum(1, 2))

# Python vs  GO
# from ctypes import CDLL
# import ctypes
# import datetime
# def speedTest():
#    sum = 0
#    for i in range(1000000):
#        sum += i
#        return sum
# if __name__ == "__main__":
#    test = CDLL("./sum.so").Test
#    test.restype = ctypes.c_int64
#    start = datetime.datetime.now()
#    for i in range(10):
#        test()
#    end = datetime.datetime.now()
#    print(end - start)
#    start = datetime.datetime.now()
#    for i in range(10):
#        speedTest()
#    end = datetime.datetime.now()
#    print(end - start)
#    print("done")