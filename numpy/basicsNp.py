#Author CM
# python3 basicNp.py
# np functions slicing dicing
import numpy as np
a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
print (a,b)
for i in a:
    if i%2==0:
        print (i,end=" ")
print (a+b)
print (a.size)  #finds lenght of array
a=np.array([[1,2],[4,3]])
print (a.shape) #dimentions of array
print (a)
print (np.ones((3,6)))
x=np.array([1,2,3,4])
print (x[-1]) #prints last element
x=np.array([[1,2,3],[4,5,6],[6,7,8]])
print (x)
print (x[0:3,2]) #prints 0 to 3 rows but increase rows value by two
print (x[:,1:3]) #prints colums from 1 to three
for row in x:
        print (row)
for cel in x.flat:
        print (cel)
x=np.arange(1,7).reshape(2,3)
y=np.arange(30).reshape(2,15)
print(x)
print (y)
rs=np.hsplit(y,3) #splits horizontally
print(rs[0])
rs2=np.vsplit(y,2)
print( rs2)
print("")
print((x))
for x in np.nditer(x,order='F'): #order option are : 'F' 'C' 'A' 'K'
        print(x)