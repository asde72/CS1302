import numpy as np
arr = np.zeros((4,5),int)
print(arr)
print("\n")
arr = np.insert(arr,1,7,0)
print(arr)
print("\n")
arr = np.insert(arr,1,5,1)
print("\n")
print(arr)
arr = np.delete(arr,0,0)
print("\n")
print(arr)
arr = np.delete(arr,0,1)
print("\n")
print(arr)
arr = np.sort(arr,0)
print("\n")
print(arr)
arr = np.ravel(arr,order="C")
print("\n")
print(arr)

'''
Creates an ndarray of shape (4, 5) where each element = 0.
Inserts a new row after the first row, where each element of the new row = 7
Inserts a new column after the first column, where each element of the new column = 5
Deletes the first row
Deletes the first column
Sorts the array along the columns in ascending order
Flattens the ndarray based on ‘row-major’ order and prints the flattened array
    





'''