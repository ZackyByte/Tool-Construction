from ctypes import *

def message(str1):
	lent = len(str1)
	print('#'*(lent+4))
	print('# '+str1+' #')
	print('#'*(lent+4))


libfunc = CDLL('/home/zacky/Documents/ISSWinter21/ToolConstruction/Labs/pythongroup/libfunc.so')
ret = libfunc.divide(100, 8)
print('Returned value: ', ret)
libfunc.divide.restype = c_float
ret = libfunc.divide(100, 8)
print('Returned value: ', ret)
ret = libfunc.divide(100, 7)
print('Returned value: ', ret)

libfunc.multiply.argtypes = [c_int, c_float, c_int]
libfunc.multiply(10, 20, 30)

try:
	libfunc.multiply(10, 'aaa', 30)
except ArgumentError as e:
	print('There was an error', e)
libfunc.multiply.argtypes = [c_int, c_int, c_int]
libfunc.multiply(10, 20, 30)
libfunc.multiply.restype = None
libfunc.multiply(10, 20, 30)
mystr2 = "WHY aren't the lines below this getting evaluated??? HOW can the code be fixed to resolve this?????"
message(mystr2)
libfunc.divide.argtypes = [c_float, c_int]
ret = libfunc.divide(33.4, 5)
print(type(ret), ret)
libfunc.divide.argtypes = [c_int, c_int]
ret = libfunc.divide(20, 3)
print(type(ret), ret)

