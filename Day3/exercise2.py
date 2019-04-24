import numpy as np
a = np.array([1,2,3])
print(a)
a1 = np.array([[1,2],[3,4]])
print(a1)
a2 = np.array([[1,2,3,4],[2,3,4,5]], ndmin =1)
print(a2)
a3 = np.array([1,2,3,4], ndmin=3)
print(a3)
a4 = np.dtype(np.int32)
print(a4)
a5 = np.array([1,2,3], dtype=complex)
print(a5)

# user defined data type
a6 = np.dtype([('age', np.int8)])
print(a6)
a7 = np.array([(10,),(20,),(30,)], dtype= a6)
print(a7['age'])
print(a7)
print(a7[0])
print(a7[0]['age'])