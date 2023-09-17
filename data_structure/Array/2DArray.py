import numpy as np

# Assuming two_array has a shape of (3, ?)
# two_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# # Create a new array with a matching number of columns (3) to insert
# new_row = np.array([1, 2, 3])

# # Insert the new row into two_array along axis 0 (rows)
# newTwoArray = np.insert(two_array, 0, new_row, axis=1)

# print(newTwoArray)


# ////////////////// inserting element in 2D array
# import numpy as np

# twoDArray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 12, 23, 13], [56, 23, 76, 43]])
# # print(twoDArray)

# newArray = np.insert(twoDArray, len(twoDArray), [[0, 0, 0, 0]], axis=1)
# print(newArray)


# ///////////////////////////// Accessing the element from the Array

# twoDArray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 12, 23, 13], [56, 23, 76, 43]])

# def accessElement(array,key):
#     for row in range(0,len(twoDArray)):
#         for col in range(0,len(twoDArray)):
#             if(key==array[row][col]):
#                 return row, col
#             # else:
#             #     return "not found"

# ans = accessElement(twoDArray,43)
# print(ans)

# second way/////////

# def accessElemen(array,rowIndex,colIndex):
#     if rowIndex >= len(array) and colIndex>=len(array[0]):
#         return "not found"
#     else:
#        return array[rowIndex][colIndex]

# ans = accessElemen(twoDArray,3,3)
# print(ans)


# ///////////////////////////////////////////traversing the two d. Array
# twoDArray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 12, 23, 13], [56, 23, 76, 43]])

# def Traverse2DArray(array):
#     for row in range(len(twoDArray)):
#         for col in range(len(twoDArray[0])):
#             print(array[row][col])

# Traverse2DArray(twoDArray)


# ///////////////////////////////////////searching the element from the array
# twoDArray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 12, 23, 13], [56, 23, 76, 43]])

# def searchElement(array,value):
#     for i in range(len(array)):
#         for j in range(len(array[0])):
#             if(value==array[i][j]):
#                 return i, j
#     return "element is not found"
# print(searchElement(twoDArray,3))



# ///////////////////////////////////////deleting the element from the array
# twoDArray = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 12, 23, 13], [56, 23, 76, 43]])
# print(twoDArray)

# newTwoDArray = np.delete(twoDArray,0,axis=1)
# print(newTwoDArray)