import numpy as np

arr = np.array([[1,2],[2,3]])
print(type(arr))
print(arr.shape)
print(arr)
print(arr.size)
print(arr[1,1])
#acess first row only
print(arr[0,:])
#aces first row size
print(arr[0,:]).size