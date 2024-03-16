import numpy as np
a=np.array([(1,2,3),(4,5,6),(1,1,1)])
print(a)
#  a=a.reshape(3,2)
#  print(a)
#  to find sum of rows
# print(a.sum(axis=1))
#  to find sum of all element of colomn
# print(a.sum(axis=0))
#  to find sqrt of all element of numy array
# print(np.sqrt(a))
# to find standard deviation
# print(np.std(a))
# arthimatic operation
# print(a+a)
# print(a-a)
# print(a*a)
# print(a/a)
# print(a%a)
# concatination is also called vertical stacking and horizontal stacking
# print(np.hstack((a,a)))
# print(np.vstack((a,a)))
# to print all element in single coloumn
print (a.ravel())



