# An array is basically a data structure which can hold more than one value at a time. It is a collection or ordered series of 
# elements of the same type.
# from array import *
import array as arr

arr = arr.array('d',[2.00,3.1,4.6,9.0456])
print(arr[2])
print(len(arr))

arr.append(5.90)
print(arr)

arr.insert(5,9.00)
print(arr)

arr.insert(1,1.0001)
print(arr)

arr.extend([1.08,9.09,8.08,10.10])
print(arr)


