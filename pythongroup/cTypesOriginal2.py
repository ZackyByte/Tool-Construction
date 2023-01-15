from ctypes import *

def message(str1):
	lent = len(str1)
	print('#'*(lent+4))
	print('# '+str1+' #')
	print('#'*(lent+4))

libfunc = CDLL('/home/zacky/Documents/ISSWinter21/ToolConstruction/Labs/pythongroup/libfunc.so')
libfunc.divide.argtypes = [c_int, c_int] #explicitly state integer for c_types for all divide functions below
libfunc.multiply.argtypes = [c_int, c_int, c_int] #c_float changed it, no argument is float in multiply functions. 
libfunc.divide.restype = c_float #state return type for all divide functions
libfunc.multiply.restype = None # moved to top for all multiply functions as a matter of best practice. this does not change output. 
ret = libfunc.divide(100, 8)
print('Returned value: ', ret)
#libfunc.divide.restype = c_float #commented out, divide restype is at the top now, since the c_float return type doesnt change. 
ret = libfunc.divide(100, 8)
print('Returned value: ', ret)
ret = libfunc.divide(100, 7)
print('Returned value: ', ret)


libfunc.multiply(10, 20, 30)

try:
	libfunc.multiply(10, 20, 30) #changed 'aaa' to 20 to avoid ArgumentError.
except ArgumentError as e:
	print('There was an error', e)
#libfunc.multiply.argtypes = [c_int, c_int, c_int] # redundant with line 18, commented out
libfunc.multiply(10, 20, 30)
libfunc.multiply(10, 20, 30)
mystr2 = "WHY aren't the lines below this getting evaluated??? HOW can the code be fixed to resolve this?????" 
message(mystr2)
#libfunc.divide.argtypes = [c_int, c_int] # at the top now, since float values do not work in the divide function.
libfunc.divide(33, 5) #changed 33.4 to 33 since floats do not work. 
libfunc.divide(20, 3)
