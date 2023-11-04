# there are four types of linked lists
# 1.  Singly Linked Lists
# 2.  Circular Singly Linked Lists
# 3.  Doubly Linked Lists
# 4.  Circular Doubly Linked lists


# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None


# class LinkedList:
#     def __init__(self,value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length=1

# new_Linked_list = LinkedList(120)
# print(new_Linked_list.tail.value)
# print(new_Linked_list.length)


# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = Node

# class LinkedList:
#     def __init__(self,value):
#         new_node = Node(value)
#         self.head=new_node
#         self.tail= new_node
#         self.length=1

# new_Linked_list = LinkedList(10)
# print(new_Linked_list.head.value)

# //////////////////////inserting element

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def __str__(self):
#         temp_node = self.head
#         result = ""
#         while temp_node:
#             result += str(temp_node.value)
#             if temp_node.next:
#                 result += "->"
#             temp_node = temp_node.next
#         return result

#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#         self.length += 1

#     def prepend(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#         self.length += 1

#     def insert(self, index, value):
#         new_node = Node(value)
#         if index < 0 or index > self.length:
#             return False
#         elif self.length==0:
#             self.head = new_node
#             self.tail = new_node
#         elif index == 0:
#             new_node.next = self.head
#             self.head = new_node
#         else:
#             temp_node = self.head
#             for _ in range(index - 1):
#                 temp_node = temp_node.next
#             new_node.next = temp_node.next
#             temp_node.next = new_node
#         self.length += 1
#         return True

#     def TraversalLinkedList(self):
#         current = self.head
#         while current:
#             print(current.value)
#             current = current.next

#     def search(self,target):
#         current = self.head
#         index = 1
#         while current:
#             if current.value==target:
#                 return index
#             current = current.next
#             index += 1
#         return -1

#     def get(self, index):
#         if index == -1:
#             return self.tail.value
#         if index < -1 or index > self.length:
#             return None
#         current = self.head
#         for _ in range(index):
#             current = current.next
#         return current.value

#     def set_value(self,index,value):  #Update value
#         temp_node = self.head
#         for _ in range(index):
#             temp_node = temp_node.next
#         if temp_node:
#             temp_node.value = value
#             return True
#         return False

#     def pop_first(self):  #remove first node and return
#         if self.length==0:
#             return None
#         popped_node = self.head
#         if self.length==1:
#             self.head = None
#             self.tail = None
#         else:
#             self.head = self.head.next
#             popped_node.next = None
#         self.length-=1
#         return popped_node.value

#     def pop(self):
#         if self.length==0:
#             return None
#         popped_node = self.tail
#         if self.length == 1:
#             self.head = self.tail = 1
#         else:
#             temp_node = self.head
#             while temp_node.next is not self.tail:
#                 temp_node = temp_node.next
#             self.tail = temp_node
#             temp_node.next = None
#         self.length-=1
#         return popped_node.value

#     def remove(self,index):
#         prev_node = self.head
#         if index ==0:
#             self.head = self.head.next
#             prev_node.next = None
#         else:
#             for _ in range(index-1):
#                 prev_node = prev_node.next
#             popped_node = prev_node.next
#             prev_node.next = popped_node.next
#             popped_node.next = None
#             self.length-=1

#     def Delete_All(self):
#         self.head = None
#         self.tail = None
#         self.length= 0

# new_linked_list = LinkedList()
# new_linked_list.prepend(10)
# new_linked_list.append(20)
# new_linked_list.append(30)
# new_linked_list.append(40)
# new_linked_list.append(50)
# # new_linked_list.insert(4, 60)
# # print(new_linked_list)
# # new_linked_list.traversal()
# # print(new_linked_list.search(60))
# # print(new_linked_list.get(-1))
# # new_linked_list.set_value(3,100)
# # print(new_linked_list.pop_first())
# # print(new_linked_list.pop())
# # new_linked_list.remove(4)
# print(new_linked_list)
# new_linked_list.Delete_All()
# print(new_linked_list)


################################################ Practice Linked list #############################################


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 1

    def __str__(self):
        firstNode = self.head
        result = ""
        while firstNode:
            result += str(firstNode.value)
            if firstNode.next:
                result += "-->"
            firstNode = firstNode.next
        return result

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def insertNode(self, value, index):
        if index < 0 or index > self.length:
            return False
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        elif index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            pre_node = self.head
            for _ in range(index - 1):
                pre_node = pre_node.next
            newNode.next = pre_node.next
            pre_node.next = newNode
        self.length += 1
        return True

    def traverseNode(self):
        newNode = self.head
        while newNode:
            print(newNode.value)
            newNode = newNode.next

    def searchNode(self, nodeValue):
        firstNode = self.head
        index = 0
        while firstNode:
            if firstNode.value == nodeValue:
                return index
            firstNode = firstNode.next
            index += 1
        return -1

    def get(self, index):
        if index < -1 or index > self.length:
            return None
        if index == -1:
            return self.tail.value
        targetNode = self.head
        for _ in range(index):
            targetNode = targetNode.next
        return targetNode.value

    def set_value(self, index, newNode):
        if index < 0 or index > self.length:
            return None
        firstNode = self.head
        for _ in range(index):
            firstNode = firstNode.next
        firstNode.value = newNode
        return "successfully updated"

    def pop_node(self):
        popedNode = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popedNode.next = None
        return popedNode.value

    def pop(self):
        popNode = self.tail
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            newNode = self.head
            while newNode.next is not self.tail:
                newNode = newNode.next
            self.tail = newNode
            newNode.next = None
        return popNode.value
    
    def remove(self,index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.next = None
        else:
            newNode = self.head
            for _ in range(index-1):
                newNode = newNode.next
            newNode.next = newNode.next.next
            popped_node = newNode.next
            newNode.next = popped_node.next
            popped_node = None
            self.length-=1
            


newLinkedList = LinkedList()
newLinkedList.append(20)
newLinkedList.append(17)
newLinkedList.append(34)
newLinkedList.append(45)
newLinkedList.prepend(34)
newLinkedList.insertNode(12, 4)
# newLinkedList.traverseNode()
# print(newLinkedList.searchNode(34))
# print(newLinkedList.get(-1))
newLinkedList.set_value(0, 40)
# print(newLinkedList.pop_node())
# print(newLinkedList.pop())
print(newLinkedList)
newLinkedList.remove(1)
print(newLinkedList)


#################################################  Practice Above things once again ################################
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def __str__(self):
#         tempNode = self.head
#         result = " "
#         while tempNode:
#             result += str(tempNode.value)
#             if tempNode.next:
#                 result += "->"
#             tempNode = tempNode.next
#         return result

#     # append the element
#     def append(self, value):
#         newNode = Node(value)
#         if self.length == 0:
#             self.head = newNode
#             self.tail = newNode
#         else:
#             self.tail.next = newNode
#             self.tail = newNode
#         self.length += 1

#     # prepend the element
#     def prepend(self, value):
#         newNode = Node(value)
#         if self.head is None:
#             self.head = newNode
#             self.tail = newNode
#         else:
#             newNode.next = self.head
#             self.head = newNode
#         self.length += 1

#     # insert element
#     def insert(self, index, value):
#         if index < 0 or index > self.length:
#             return None
#         newNode = Node(value)
#         if index == 0:
#             newNode.next = self.head
#             self.head = newNode
#         else:
#             prevNode = self.head
#             for _ in range(index - 1):
#                 prevNode = prevNode.next
#             newNode.next = prevNode.next
#             prevNode.next = newNode
#         self.length += 1

#     # Taverse the element
#     def Traverse(self):
#         tempNode = self.head
#         while tempNode:
#             print(tempNode.value)
#             tempNode = tempNode.next

#     # Search the element
#     def Search(self, target):
#         tempNode = self.head
#         while tempNode:
#             if tempNode.value == target:
#                 return True
#             tempNode = tempNode.next
#         return False

#     # get the element with index
#     def get(self, index):
#         if index < 0 or index > self.length:
#             return None
#         tempNode = self.head
#         for _ in range(index):
#             tempNode = tempNode.next
#         return tempNode.value

#     #update the value
#     def set_value(self,index,value):
#         tempNode = self.head
#         for _ in range(index):
#             tempNode = tempNode.next
#         if tempNode:
#             tempNode.value = value
#         return False

#     # delete first node
#     def pop_first(self):
#         tempNode = self.head
#         if self.length==0:
#             print("nothing to delete")
#         elif self.length == 1:
#             self.head = None
#             self.tail = None
#         else:
#             self.head = tempNode.next
#             tempNode.next = None
#         self.length-=1

#     def pop(self):
#         if self.length==0:
#             print("nothing to delete")
#         elif self.length==1:
#             self.head = None
#             self.tail = None
#         else:
#             tempNode = self.head
#             while tempNode is not self.tail:
#                 tempNode = tempNode.next
#             tempNode.next = None
#             self.tail = tempNode
#         self.length-=1

#     # remove element from list
#     def remove(self,index):
#         tempNode = self.head
#         if self.length == 0:
#             print("nothing to delete")
#         elif index==1:
#             self.head = tempNode.next
#             tempNode.next = None
#         else:
#             for _ in range(index-1):
#                 tempNode = tempNode.next
#             poppedNode = tempNode.next
#             tempNode.next = poppedNode.next
#             poppedNode.next = None

#         self.length-=1

#     # delete All node
#     def DeleteAll(self):
#         self.head = None
#         self.tail = None
#         self.length = 0


# new_linked_list = LinkedList()
# new_linked_list.append(20)
# new_linked_list.append(30)
# new_linked_list.append(40)
# new_linked_list.prepend(10)
# new_linked_list.insert(4, 60)
# print(new_linked_list)
# # new_linked_list.Traverse()
# # print(new_linked_list.Search(20))
# # print(new_linked_list.get(3))
# # new_linked_list.set_value(4,100)
# # new_linked_list.pop_first()
# # new_linked_list.pop()
# # new_linked_list.remove(2)
# new_linked_list.DeleteAll()
# print(new_linked_list)
