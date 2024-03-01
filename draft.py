import numpy as np
import string as st
arr = np.array([1,3,5,6,7,8,9,3,5,6,4,2]) 
newarr = arr.reshape(2,2,-1)

print(newarr)
for x in np.ndenumerate(newarr):
    print(x)

# print(newArr)
# for x in newArr:
#     # print(x)
#     for y in x:
#         for z in y:
#             print(z)


