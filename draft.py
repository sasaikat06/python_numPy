
import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]])

# newarr = np.hsplit(arr,3)

# print(newarr)




# sort() method returns a copy of the array, leaving the original array unchanged
# print(arr.shape)
# newarr = arr.reshape(2,-1)
# print(newarr)
# print(np.sort(newarr))
arr = np.array([13,5,6,76])

# check = [True,False,True,False]

fileter_arr = []

for element in arr:
    if element%2 == 1:
        fileter_arr.append(True)
    else:
        fileter_arr.append(False)
newarr = arr[fileter_arr]
newarr1 = arr[sorted(fileter_arr)]
print(sorted(fileter_arr))
print(fileter_arr)
print(sorted(newarr))
print(newarr1)