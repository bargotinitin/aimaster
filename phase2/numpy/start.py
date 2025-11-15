import numpy as np


print(np.__version__)

arr = np.array([1, 3, 23, 44])

print(arr)

print(arr[0])

print(arr[1])


arr1=np.array([[90,23,23,2323,23],[1,2,3,9032,23]])
print(arr1.shape)

# for x in arr1:
# 	for y in x:
	 #print(y)


arr2=np.array([[90,23,23,2323,23],[1,2,3,9032,23],[1,2,3,8,23]])
print(arr2.shape)

for z in np.nditer(arr2):
    print(z)
