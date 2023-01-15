from ctypes import *

def message(str1):
	lent = len(str1)
	print('#'*(lent+4))
	print('# '+str1+' #')
	print('#'*(lent+4))

libfunc = CDLL('/home/zacky/Documents/ISSWinter21/ToolConstruction/Labs/pythongroup/libfunc.so')
libfunc.divide.restype = c_float
ret = libfunc.divide(100, 8)
#libfunc.divide.restype = c_float #added to stop program from guessing ctype as int instead of float.
print('Returned value: ', ret)
ret = libfunc.divide(100, 8)
print('Returned value: ', ret)
ret = libfunc.divide(100, 7)
print('Returned value: ', ret)

libfunc.multiply.argtypes = [c_int, c_int, c_int]
libfunc.multiply(10, 20, 30)

try:
	libfunc.multiply(10, 20, 30) #changed 'aaa' to 20 as per libfunc.multiply line 19
except ArgumentError as e:
	print('There was an error', e)
libfunc.multiply(10, 20, 30)
libfunc.multiply.restype = c_int #changed to c_int from none
libfunc.multiply(10, 20, 30)
mystr2 = "WHY aren't the lines below this getting evaluated??? HOW can the code be fixed to resolve this?????"
message(mystr2)
libfunc.divide.argtypes = [c_int, c_int] #added line argtypes for libfunc divide 
ret = libfunc.divide(33, 5)

print('Returned value: ', ret)				#added ret to store result in variable
libfunc.divide.argtypes = [c_int, c_int]	#added line argtypes for libfunc divide
ret = libfunc.divide(20, 3)					#added ret to store result in variable
print('Returned value: ', ret)

