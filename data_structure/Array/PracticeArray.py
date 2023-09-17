# import numpy as np

# myArray = np.array([1,2,3,4,5])

# print(myArray)
# print(myArray[1])

# def findArray(array):
#     for i in range(len(myArray)):
#         print(array[i])

# findArray(myArray)

# ////////////////insertion 

# for i in myArray:
#     print(i)
 



# import array

# myArray = array.array('i',[1,2,3,4,6])
# print(myArray)

# myArray.insert(4,12)
# myArray.append(23)/
# # 
# def accessElement(array,k):
#     if(k>len(array)):
#         return "out of the range"
#     else:
#         for i in range(len(array)):
#             if(k==array[i]):
#                 return i
            
# ans = accessElement(myArray,421)

# print(ans)








# ?////////////////////////////////////////////////////////////////////////////   Two Dimentional Array

import numpy as np

myArray = np.array([[11,21,43,56],[56,32,76,43],[67,43,73,87],[76,23,98,33]])
# print(myArray)

# ////////////////// insertion in two d Array

# newArray = np.insert(myArray,3,[[1,2,3,4]],axis=0)
# print(newArray)

# ////////////////// deletion in two d Array

# newArray = np.delete(myArray,0,axis=0)
# print(newArray)

# ///////////////////////accessing element in array

# import numpy as np

# myArray = np.array([[11,21,43,56],[56,32,76,43],[67,43,73,87],[76,23,98,33]])

# def accessArray(array,value):
#     for row in range(len(array)):
#         for col in range(len(array[0])):
#             if(array[row][col]==value):
#                 return row, col
# ans = accessArray(myArray,87)
# print(ans)


# /////////////////////////  Travering Two D Array
# import numpy as np

# myArray = np.array([[11,21,43,56],[56,32,76,43],[67,43,73,87],[76,23,98,33]])

# def TraverArray(array):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             print(array[i][j])
# TraverArray(myArray)