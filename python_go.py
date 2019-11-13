
from ctypes import CDLL
add = CDLL('./hello.so').addstr # 调用go模块

# 显式声明参数和返回的期望类型
add.argtypes =[ctypes.c_char_p,ctypes.c_char_p]

add.restype = ctypes.c_char_p
print(add("hhh",'eee'))


# 无参数，则可直接调用
t = CDLL('./hello.so').test # 调用go模块

print(t())