import numpy as np
import string as st
arr = np.array([[1,2],[3,4]]) 
arr2 = np.array([[5,6],[7,8]])
# print(set(arr2))
print("real concate",np.concatenate((arr,arr2)))
print("concate:",np.concatenate((arr,arr2),axis=1))
print("Stack:",np.stack((arr,arr2),axis=1))
print("hstack",np.hstack((arr,arr2)))
print("vstack",np.vstack((arr,arr2)))
print("dstack",np.dstack((arr,arr2)))

# print(newArr)
# for x in newArr:
#     # print(x)
#     for y in x:
#         for z in y:
#             print(z)


