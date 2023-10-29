# import array

# my_array = array.array('i')
# print(my_array)

# my_array2 = array.array('i', [1,2,3,4])
# print(my_array2)


# import numpy as np

# my_array = np.array([1,12,2])
# print(my_array)


# ////////////////////insertion

# from array import *

# my_array = array('i',[1,2,3,4,5])
# print(my_array)

# my_array.insert(0,6)
# print(my_array)

# def printArray(array):
#     for i in range(0,6):
#         print(my_array[i])

# printArray(my_array)

# //////////////////////accessing element from array

# def funAccess(array,k):
#    if(k>len(array)):
#       return "not found"
#    else:
#        for i in range(0,len(array)):
#         if(k==array[i]):
#             return i

# print(funAccess(my_array,213))
#

# /////////////////////// deleting the array


# from array import *

# my_array = array('i',[1,2,3,4,5])

# my_array.remove(4)
# print(my_array)


############################################################ practice  ##########################


# import array

# my_array = array.array('i',[2,3,4,5])
# print(my_array)

# import numpy as np

# my_array = np.array([11,23,54,23,45])
# print(my_array)

# //////////////////////  insertion
from array import *

my_array = array("i", [1, 3, 5, 7, 42, 5, 6, 8, 45])
my_array.insert(0, 8)

# ////////////   accessing the element


def accessElem(arr, k):
    if k > len(arr):
        return "not found"
    for i in range(0, len(arr)):
        if k == arr[i]:
            return i

print(accessElem(my_array, 45))
