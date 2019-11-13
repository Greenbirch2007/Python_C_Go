# coding:utf-8

import time
from ctypes import CDLL
import ctypes

def xu():
    sum = 0
    for i in range(0,10000+1):
        sum += i
    return sum

if __name__ =="__main__":
    add = CDLL('./hello.so').addstr #调用ｇｏ模块addstr方法
    # 显式声明参数和返回的期望类型
    add.argtypes=[ctypes.c_char_p,ctypes.c_char_p]
    add.restype =ctypes.c_char_p
    print(add("a","e"))

    # go 一百万次累加
    start = time.time()
    t = CDLL('./hello.so').test #调用ｇｏ模块test方法
    t.restype = ctypes.c_int64 # 返回int64类型
    print("go执行结果：%s" % t())
    end = time.time()
    print("go :1000000 累加耗时 %.2f" % (end - start))
​
# python累加一百万次
start = time.time()
print("python执行结果：%s" % xu())
end = time.time()
print("python :1000000 累加耗时 %.2f" % (end - start))
​
