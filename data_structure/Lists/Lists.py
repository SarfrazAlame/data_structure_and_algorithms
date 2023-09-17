# shoppingList = ["milk","curd","apple","orange"]

# print(shoppingList[1])
# print(shoppingList[-1])
# print('mildk' in shoppingList)

# for i in shoppingList:
#     print(i)

# for i in range(len(shoppingList)):
#     print(shoppingList[i])

# shoppingList[2] = "guava"
# print(shoppingList)


# myList = [1,2,3,4]
# print(myList)

# myList.insert(2,12)
# print(myList)

# myList.append(13)
# print(myList)

# newList = [1,2,3]
# myList.extend(newList)
# print(myList)


myLists = ["a", "b", "c", "d", "e", "f"]

# newList = myLists[0:2]
# print(newList)

# print(myLists[3:])
# print(myLists[:])

# myLists.pop(1)

# print(myLists.pop())
# print(myLists)

# del myLists[1]

# del myLists[0:3]
# del myLists[2:5]
# print(myLists)

# myLists.remove('a')
# print(myLists)

# myLists = [10, 20, 30, 40, 50]

# target = 210
# # if target in myLists:
# #     print(f"{target} is in list")
# # else:
# #     print(f"{target} is not in the")
# # or?

# def linear_search(p_list, target):
#     for i in range(len(p_list)):
#         if target == p_list[i]:
#             return f"{target} is present"
#         else:
#             return f"{target} is not present"


# ans = linear_search(myLists, target)
# print(ans)


# a = [1,2,3]
# b = [4,5,7]

# print(a+b)


# ///////////////////////////string and lists

# a = 'spam'
# b = list(a)

# print(b)


# a = "my name is mohammad Sarfraz and i have made tauba from  all types of jina"
# b = a.split()
# print(b)

# myList = [2,7,2,9,45,12,3,5,7,45]

# # myList = myList+[23]
# myList.sort()

# print(myList)

# import numpy as np

# myArray = np.array([1,2,3,4,5,6,7])
# myLists = [2,43,5,76,8]

# print(myArray/2)
# print(myLists/2)


# ################################################List comprehension

# formula  new_lists = [new_item for i in lists]
# eg

# pre_list = [1,2,3,4,5,6]
# new_List = [i*2 for i in pre_list]
# print(new_List)

# language = 'Python'

# new_list = [letter for letter in language]
# print(new_list)


# //////////////project

# numDays = int(input("How many day's temperature "))
# total = 0
# temp = []
# for i in range(numDays):
#     nextDay = int(input("Day " + str(i + 1) + "'s high temperature: "))
#     temp.append(nextDay)    
#     total += temp[i]
# avg = round(total / numDays, 2)
# print("Average is " + str(avg))

# ans=0
# # for i in range(len(temp)):
# #     if(temp[i]>avg):
# #         ans+=1
# # or
# for i in temp:
#     if i>avg:
#         ans+=1
# print(f"{ans} day is above the average temperature")


# /////////////////////////////////////Problem  leetcode  finding the missing number from array 0 to n
# 01 Q
#  myLists = [1,2,4,5,7,8,9,10]

# def missingNumber(list,n):
#    sum1 = 10*11/2
#    sum2 = sum(list)
#    print(sum1-sum2)

# missingNumber(myLists,10)


# 02 Q find two consecutive index whose sum of value is given target
# myArrray = [1,3,5,6,7,9]
# target =  4

# def sumOfGivenArray(array,target):
#    for i in range(len(array)):
#       if(array[i]+array[i+1] == target):
#          return i,i+1
# ans = sumOfGivenArray(myArrray,target)
# print(ans)


# /////////second ways

# myArrray = [1,3,2,4,3,4]

# def findPair(array,target):
#     for i in range(len(array)):
#         for j in range(i+1,len(array)):
#             if array[i]==array[j]:
#                 continue
#             elif array[i]+array[j] == target:
#                 print(i,j)
# findPair(myArrray,6)