# class Stack:
#     def __init__(self):
#         self.list = []
    
#     def __str__(self):
#         values = self.list.reverse()
#         values = [str(x) for x in self.list]
#         return '\n'.join(values)
    
#     def isEmpty(self):
#         if self.list == []:
#             return True
#         else:
#             return False
        
#     def push(self,value):
#         self.list.append(value)
#         return "element inserted sucessfully"
    
#     def pop(self):
#         if self.isEmpty():
#             return "there is not any element to remove"
#         else:
#             return self.list.pop()
    
#     def peek(self):
#         if self.isEmpty():
#             return "There is not any element to remove"
#         else:
#             return self.list[len(self.list)-1]
    
#     def delete(self):
#         self.list = None
    
# customStack = Stack()
# # print(customStack.isEmpty())
# customStack.push(10)
# customStack.push(20)
# customStack.push(30)
# print(customStack)
# # print(" ")
# # print(customStack.pop())
# # print(customStack.pop())



################## Stack with size limit

# class Stack:
#     def __init__(self,maxValue):
#         self.maxValue = maxValue
#         self.list = []
    
#     def __str__(self):
#         values = self.list.reverse()
#         values = [str(x) for x in self.list]
#         return '\n'.join(values)
    
#     def isEmpty(self):
#         if self.list==[]:
#             return True
#         else:
#             return False
        
#     def isFull(self):
#         if len(self.list)==self.maxValue:
#             return True
#         else:
#             return False
        
#     def push(self,value):
#         if self.isFull():
#             return "stack is full"
#         else:
#             self.list.append(value)
        
#     def pop(self):
#         if self.isEmpty():
#             return "there is not any element to remove"
#         else:
#             return self.list.pop()
    
#     def peek(self):
#         if self.isEmpty():
#             return "There is not eny element to remove"
#         else:
#             return self.list[len(self.list)-1]
    
#     def delete(self):
#         self.list = None

# customStack = Stack(4)
# # print(customStack.isEmpty())
# # print(customStack.isFull())
# customStack.push(10)
# customStack.push(20)
# customStack.push(30)
# customStack.push(40)
# # print(customStack.pop())
# # print(customStack.peek())
# # print("=====")
# customStack.delete()
# print(customStack)


#################### Stack using linked list
class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next
    

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False
    
    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    
    def pop(self):
        if self.isEmpty():
            return "there is not any element to remove"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
    
    def peek(self):
        if self.isEmpty():
            return "there is not any element to remove"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
    
    def delete(self):
        self.LinkedList.head==None

customStack = Stack()
# print(customStack.isEmpty())
customStack.push(10)
customStack.push(20)
customStack.push(30)
customStack.push(40)
# print(customStack)
# print("=====")
# customStack.pop()
# print(customStack.peek())
# customStack.delete()
print(customStack)