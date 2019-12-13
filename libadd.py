from ctypes import CDLL
import ctypes

if __name__ == "__main__":
    t = CDLL("./libadd.so").Add

    print(t.Add(222, 444))