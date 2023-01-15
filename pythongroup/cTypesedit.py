from ctypes import *

def message(str1):
    lent = len(str1)
    print('#'*(lent+4))
    print('# '+str1+' #')
    print('#'*(lent+4))

libfunc = CDLL('/home/zacky/Documents/ISSWinter21/ToolConstruction/Labs/pythongroup/libfunc.so')
libfunc.divide.restype = c_float #libfunc.divide.restype moved to the top, specifying a c_float for the function
ret = libfunc.divide(100, 8)
print('Returned value: ', ret)
ret = libfunc.divide(100, 8)
print('Returned value: ', ret)
ret = libfunc.divide(100, 7)
print('Returned value: ', ret)

libfunc.multiply.argtypes = [c_int, c_int, c_int] 
libfunc.multiply(10, 20, 30)

try:
    libfunc.multiply(10, 'aaa', 30) #'aaa' is not c_int type, but the code still executes. 
except ArgumentError as e:
    print('There was an error', e)

libfunc.multiply(10, 20, 30)
libfunc.multiply.restype = None
ret = libfunc.multiply(10, 20, 30)
mystr2 = "WHY aren't the lines below this getting evaluated??? HOW can the code be fixed to resolve this?????"
message(mystr2)
libfunc.divide.argtypes = [c_int, c_int]
ret = libfunc.divide(33, 5)
print('Returned value: ', ret)
libfunc.divide.argtypes = [c_int, c_int]
ret = libfunc.divide(20, 3)
print('Returned value: ', ret)