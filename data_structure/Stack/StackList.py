# class Stack:
#     def __init__(self):
#         self.list = []

#     def __str__(self):
#         values = self.list.reverse()
#         values = [str(x) for x in self.list]
#         return '\n'.join(values)

#     # is Empty
#     def isEmpty(self):
#         if self.list == []:
#             return True
#         else:
#             return False

#     # push
#     def push(self,value):
#         self.list.append(value)
#         return "the element has been successfully inserted"

#     # pop
#     def pop(self):
#         if self.isEmpty():
#             return "There is not any element to stack"
#         else:
#             return self.list.pop()

#     #peek
#     def peek(self):
#         if self.isEmpty():
#             return "There is not any element in the stack"
#         else:
#             return self.list[len(self.list)-1]

#     # delete
#     def delete(self):
#         self.list = None


# customStack = Stack()
# # print(customStack.isEmpty())
# customStack.push(10)
# customStack.push(20)
# customStack.push(30)
# # print(customStack.pop())
# print(customStack.peek())


#############  Stack with size limit

# class Stack:
#     def __init__(self,maxValue):
#         self.maxValue = maxValue
#         self.list = []

#     def __str__(self):
#         values = self.list.reverse()
#         values = [str(x) for x in self.list]
#         return '\n'.join(values)

#     # isEmpty
#     def isEmpty(self):
#         if self.list == []:
#             return True
#         else:
#             return False

#     # isFull
#     def isFull(self):
#         if len(self.list)==self.maxValue:
#             return True
#         else:
#             return False

#     # push
#     def push(self,value):
#         if self.isFull():
#             return "The Stack is full"
#         else:
#             self.list.append(value)
#             return "The element has been successfully inserted"

#     # pop
#     def pop(self):
#         if self.isEmpty():
#             return "There is not any element to remove"
#         else:
#             return self.list.pop()

#     # peek
#     def peek(self):
#         if self.isEmpty():
#             return "There is not any element to remove"
#         else:
#             return self.list[len(self.list)-1]

#     # delete
#     def delete(self):
#         self.list = None


# customStack = Stack(4)
# # print(customStack.isEmpty())
# # print(customStack.isFull())
# customStack.push(10)
# customStack.push(20)
# customStack.push(30)
# customStack.push(40)
# print(customStack)

###########################  Stack using Linked List


class Node:
    def __init__(self, value=None):
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
        return "\n".join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "There is not any element to remove"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
    def peek(self):
        if self.isEmpty():
            return "There is not any element to remove"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
    
    def delete(self):
        self.LinkedList.head=None


customStack = Stack()
# print(customStack.isEmpty())
customStack.push(10)
customStack.push(20)
customStack.push(30)
# print(customStack)
# print("-------------")
# print(customStack.pop())
customStack.delete()
print(customStack.peek())
