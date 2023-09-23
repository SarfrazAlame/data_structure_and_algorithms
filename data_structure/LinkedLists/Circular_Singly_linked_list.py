# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None


# class CSLinkedList:
#     # def __init__(self,value):
#     #     new_node = Node(value)
#     #     new_node.next = new_node
#     #     self.head = new_node
#     #     self.tail = new_node
#     #     self.length = 1

    # def __init__(self):
    #     self.head = None
    #     self.tail = None
    #     self.length = 0

#     def __str__(self):
#         temp_node = self.head
#         result = ""
#         while temp_node is not None:
#             result += str(temp_node.value)
#             temp_node = temp_node.next
#             if temp_node == self.head:
#                 break
#             result += "->"
#         return result

#     def append(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#             new_node.next = new_node
#         else:
#             self.tail.next = new_node
#             new_node.next = self.head
#             self.tail = new_node
#         self.length += 1

#     def preppend(self, value):
#         new_node = Node(value)
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#             new_node.next = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#             self.tail.next = new_node
#         self.length += 1

#     def insertion(self, index, value):
#         new_node = Node(value)
#         if index < 0 or index > self.length:
#             return None
#         elif self.head is None:
#             self.head = new_node
#             self.tail = new_node
#             new_node.next = new_node
#         elif index == 0:
#             new_node.next = self.head
#             self.tail.next = new_node
#             self.head = new_node
#         elif index == self.length:
#             self.tail.next = new_node
#             new_node.next = self.head
#             self.tail = new_node
#         else:
#             current = self.head
#             for _ in range(index - 1):
#                 current = current.next
#             new_node.next = current.next
#             current.next = new_node
#         self.length += 1

#     def traversal(self):
#         current = self.head
#         while current:
#             print(current.value)
#             current = current.next
#             if current == self.head:
#                 break

#     def search(self, target):
#         current = self.head
#         while current:
#             if current.value == target:
#                 return True
#             current = current.next
#             if current == self.head:
#                 break
#         return False

#     def get(self, index):
#         if index < 0 or index > self.length:
#             return None
#         current = self.head
#         for _ in range(index):
#             current = current.next
#         return current.value

#     def set_value(self, index, value):
#         temp_node = self.head
#         for _ in range(index):
#             temp_node = temp_node.next
#         if temp_node:
#             temp_node.value = value

#     def pop_first(self):
#         currrent = self.head
#         if self.length == 1:
#             self.head = None
#             self.tail = None
#         else:
#             self.head = currrent.next
#             self.tail.next = currrent.next
#             currrent.next = None
#             self.length -= 1
#         return currrent.value

#     def pop(self):
#         popped_node = self.tail
#         temp_node = self.head
#         if self.length == 0:
#             return None
#         elif self.length==1:
#             self.head=None
#             self.tail=None
#         else:
#             while temp_node is not self.tail:
#                 temp_node = temp_node.next
#             self.tail = temp_node
#             temp_node.next=self.head
#             popped_node.next = None
#         self.length-=1
#         return popped_node.value

#     def remove(self,index):
#         prev_element = self.head
#         if index == 0:
#             self.head = prev_element.next
#             self.tail.next = prev_element.next
#             prev_element.next = None
#         else:
#             for _ in range(index-1):
#                 prev_element=prev_element.next
#             removed_node = prev_element.next
#             prev_element.next = removed_node.next
#             removed_node.next = None
#             self.length-=1


#     def delete_all(self):
#         self.tail.next = None
#         self.head = None
#         self.tail = None
#         self.length = 0


# cslinkedList = CSLinkedList()
# cslinkedList.append(10)
# cslinkedList.append(20)
# cslinkedList.append(30)
# cslinkedList.append(40)
# cslinkedList.preppend(60)
# cslinkedList.insertion(5, 200)
# print(cslinkedList)
# # cslinkedList.traversal()
# # print(cslinkedList.search(202))
# # print(cslinkedList.get(1))
# # cslinkedList.set_value(5,100)
# # print(cslinkedList.pop_first())
# # print(cslinkedList.pop())
# # cslinkedList.remove(0)
# cslinkedList.delete_all()
# print(cslinkedList)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

 
class CSLinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        self.length = 1
 
    def __str__(self):
        tempNode = self.head
        result = ""
        while tempNode is not None:
            result += str(tempNode.value)
            tempNode = tempNode.next
            if tempNode==self.head:
                break
            result += "->"
        return result
       
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            newNode.next = self.head
        self.length+=1
    
    def prepend(self,value):
        newNode = Node(value)
        if self.length==0:
            self.head = newNode
            self.head = newNode
            newNode.next = newNode
        else:
            newNode.next = self.head
            self.tail.next = newNode
            self.head = newNode
        self.length+=1
        
    def insertion(self,index,value):
        newNode = Node(value)
        if index==0:
            if self.length==0:
                self.head = newNode
                self.tail = newNode
                newNode.next = newNode
            else:
                newNode.next = self.head
                self.tail.next = newNode
                self.head = newNode
        else:
            prevNode = self.head
            for _ in range(index-1):
                prevNode = prevNode.next
            newNode.next = prevNode.next
            prevNode.next = newNode
        self.length+=1

    def Traversal(self):
        newNode = self.head
        while newNode:
            print(newNode.value)
            newNode = newNode.next
            if newNode is self.head:
                break
    
    def Search(self,target):
        tempNode = self.head
        while tempNode:
            if tempNode.value==target:
                return True
            tempNode = tempNode.next
            if tempNode is self.head:
                break
        return False
    
    def get(self,index):
        newNode = self.head
        for _ in range(index):
            newNode = newNode.next
        return newNode.value
    
    def set_value(self,index,value):
        tempNode = self.head
        for _ in range(index):
            tempNode = tempNode.next
        if tempNode:
            tempNode.value = value

    def pop_first(self):
        current = self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head = current.next
            self.tail.next = current.next
            current.next = None
        self.length-=1
        return current.value
    
    def pop(self):
        current = self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            while current is not self.tail:
                current = current.next
            self.tail.next = None
            self.tail =current
            current.next = self.head
            

nextLinkedList = CSLinkedList()
nextLinkedList.append(10)
nextLinkedList.append(20)
nextLinkedList.append(30)
nextLinkedList.append(40)
nextLinkedList.prepend(50) 
nextLinkedList.insertion(4,100)
# nextLinkedList.Traversal()
# print(nextLinkedList.Search(100))
# print(nextLinkedList.get(4))
# nextLinkedList.set_value(4,200)
# print(nextLinkedList)
# print(nextLinkedList.pop_first())
print(nextLinkedList)
nextLinkedList.pop()
print(nextLinkedList)
