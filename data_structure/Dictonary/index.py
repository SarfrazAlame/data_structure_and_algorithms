# my_dict = dict()
# print(my_dict)

# my_dict2 = {}
# print(my_dict2)

# eng_sp = dict(one="uno", two="dos", tree="tres")
# print(eng_sp)

# eng_sp2 = {"one": "uno", "two": "dos", "thres": "tres"}
# print(eng_sp2)

# eng_sp3 = [("one", "uno"), ("two", "dos"), ("thres", "tres")]
# eng_sp4 = dict(eng_sp3)
# print(eng_sp4)

# myDetais = {'name':"sarfraz khan", 'age':21}
# myDetais['age'] = 22
# print(myDetais)
# print(myDetais['name'])
# print(myDetais['age'])
# myDetais['address'] = "London"
# print(myDetais)

# tarversing 

# def traverseDict(dict):
#     for key in dict:
#         print(dict[key])

# traverseDict(myDetais)

#searching

# def searchingValue(dict,value):
#     for key in dict:
#         if dict[key] == value:
#             return key,value
#     return "value not exists"

# ans = searchingValue(myDetais,'London')
# print(ans)




# //////////////////////////deleting the value
# myDetais = {'name':"sarfraz khan", 'age':21,'address':"London","education":"master"}
# del myDetais['age']
# print(myDetais)

# removed_element = myDetais.pop('age')

# print(removed_element)
# print(myDetais)


# ########################################methods of dictionary

# myDetais = {'name':"sarfraz khan", 'age':21,'address':"London","education":"master"}

# myDetais.clear()
# print(myDetais)

# newDict = myDetais.copy()
# print(newDict)
# print(myDetais)

# newDict = {}.fromkeys([1,2,3],10)
# print(newDict)

# print(myDetais.get('age',22))

# print(myDetais.items())

# print(myDetais.keys())

# print(myDetais.values())


# myDetais = {'name':"sarfraz khan", 'age':21,'address':"London","education":"master"}

# print(myDetais.popitem())
# print(myDetais)

# print(myDetais.setdefault("name1","added"))
# print(myDetais)

# print(myDetais.pop("name","not"))
# print(myDetais)

# newDict = {'a':1,'b':2,'c':3}
# myDetais.update(newDict)
# print(myDetais)


# myDict = dict()
# print(myDict)

# Dict_My = {}
# print(Dict_My)

my_Dict = {"myName":"Sarfraz Khan", "age":21,"address":"London","education":"No degree"}
print(my_Dict)