# class Node:
#     def __init__(self,value=None):
#         self.value = value
#         self.next = None
#         self.prev = None
    
# class CircularDoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node
#             node = node.next
#             if node == self.tail.next:
#                 break
    
#     # Creating of Circular Doubly Linked List
#     def createCDLL(self,nodeValue):
#         newNode = Node(nodeValue)
#         self.head = newNode
#         self.tail = newNode
#         newNode.next = newNode
#         newNode.prev = newNode
#         return "the CDLL is created successfully"
    
#     def insertion(self,nodeValue,index):
#         if self.head is None:
#             return "the CDLL does not exist"
#         else:
#             newNode = Node(nodeValue)
#             if index==0:
#                 newNode.prev = self.tail
#                 newNode.next = self.head
#                 self.head.prev = newNode
#                 self.tail.next = newNode
#                 self.head = newNode
#             elif index==1:
#                 self.head.prev = newNode
#                 self.tail.next = newNode
#                 newNode.next = self.head
#                 newNode.prev = self.tail
#                 self.tail = newNode
#             else:
#                 prevNode = self.head
#                 for _ in range(index-1):
#                     prevNode = prevNode.next
#                 newNode.next = prevNode.next
#                 prevNode.next = newNode
#                 newNode.prev = prevNode
#                 prevNode.next.prev =  newNode
#             return "the element have been  inserted !"
    
#     # Traversal element in node
#     def traversal(self):
#         if self.head is None:
#             print("there is not any node to traverse")
#         tempNode = self.head
#         while tempNode:
#             print(tempNode.value)
#             tempNode = tempNode.next
#             if tempNode== self.tail.next:
#                 break
        
#     # Reverse the node in the CDLL
#     def Reversed(self):
#         if self.head is None:
#             print("There is not any node to reverse")
#         tempNode = self.tail
#         while tempNode:
#             print(tempNode.value)
#             if tempNode == self.head:
#                 break
#             tempNode = tempNode.prev

#     # Search the node in CDLL
#     def Search(self,nodeValue):
#         if self.head is None:
#             return 'there is not any node to traverse'
#         tempNode = self.head
#         while tempNode:
#             if tempNode.value==nodeValue:
#                 return tempNode.value
#             if tempNode ==self.tail:
#                 return "The Value does not exist in DLL"
#             tempNode = tempNode.next
        
#     # Deletion in DLL 
#     def Deletion(self,location):
#         if self.head is None:
#             print("There is not any element to delete")
#         if location == 0:
#             if self.head==self.tail:
#                 self.head.prev = None
#                 self.tail.next = None
#                 self.head = None
#                 self.tail = None
#             else:
#                 self.head = self.head.next
#                 self.head.prev = self.tail
#                 self.tail.next = self.head
#         elif location==1:
#             if self.head==self.tail:
#                 self.head.prev = None
#                 self.tail.next = None
#                 self.head = None
#                 self.tail = None
#             else:
#                 self.tail = self.tail.prev
#                 self.tail.next= self.head
#                 self.head.prev = self.tail
#         else:
#             preDeletedNode = self.head
#             for _ in range(location-1):
#                 preDeletedNode = preDeletedNode.next
#             preDeletedNode.next = preDeletedNode.next.next
#             preDeletedNode.next.prev = preDeletedNode
#         print("the node have been successfully deleted")
    
#     # deleteing the entire circular doubly linked list
#     def deleteAll(self):
#         if self.head is None:
#             print("there is not any node to delete")
#         else:
#             self.tail.next = None
#             tempNode = self.head
#             while tempNode:
#                 tempNode.prev = None
#                 tempNode = tempNode.next
#             self.head = None
#             self.tail = None
#             print("Deleted All node successfully")


# new_circular_doubly_linked_list = CircularDoublyLinkedList()
# new_circular_doubly_linked_list.createCDLL(20)
# new_circular_doubly_linked_list.insertion(10,0)
# new_circular_doubly_linked_list.insertion(30,1)
# new_circular_doubly_linked_list.insertion(40,1)
# new_circular_doubly_linked_list.insertion(50,1)
# print([node.value for node in new_circular_doubly_linked_list])
# # new_circular_doubly_linked_list.traversal()
# # print("   ")
# # new_circular_doubly_linked_list.Reversed()
# # print(new_circular_doubly_linked_list.Search(40))
# # new_circular_doubly_linked_list.Deletion(3)
# # print([node.value for node in new_circular_doubly_linked_list])
# new_circular_doubly_linked_list.deleteAll()
# print([node.value for node in new_circular_doubly_linked_list])


####################################  practice again  ####################################

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.pre = None

class CSDLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        newNode = self.head
        while newNode:
            yield newNode
            newNode = newNode.next
            if newNode is self.head:
                break
    
    def createNode(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = None
        newNode.pre = None
        return "ndoe created successfully"
    
    def insertNode(self, value, index):
        newNode = Node(value)
        if self.head is None:
            print("nothing to insert")
        else:
            if index == 0:
                newNode.next = self.head
                self.tail.next = newNode
                newNode.pre = self.tail
                self.head = newNode
            else:
                tempNode = self.head
                for _ in range(index-1):
                    tempNode = tempNode.next
                newNode.next = tempNode.next
                tempNode.next = newNode
                newNode.pre = tempNode
                newNode.next.pre = newNode
    
    def TraverseNode(self):
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.next
            if tempNode is self.head:
                break

    def reverseTraverseNode(self):
        tempNode = self.tail
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.pre
            if tempNode is self.tail:
                break

    def SearchNode(self,value):
        if self.head is None:
            return "nothign to search"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return True
                tempNode = tempNode.next
                if tempNode is self.head:
                    break
            return False
    
    def deleteNode(self,index):
        tempNode = self.head
        if self.head is None:
            print("nothing to delete")
        else:
            if index==0:
                self.head = tempNode.next
                self.head.pre = self.tail
                self.tail.next = self.head
                tempNode.next = None
            else:
                for _ in range(index-1):
                    tempNode = tempNode.next
                removedNode = tempNode.next
                tempNode.next = removedNode.next
                removedNode.next.pre = tempNode
                removedNode.next = None
                removedNode.pre = None


newCSDLinkedList = CSDLinkedList()
newCSDLinkedList.createNode(12)
newCSDLinkedList.insertNode(10,0)
newCSDLinkedList.insertNode(15,1)
newCSDLinkedList.insertNode(24,2)
# newCSDLinkedList.TraverseNode()
# newCSDLinkedList.reverseTraverseNode()
# print(newCSDLinkedList.SearchNode(15))
print([newNode.value for newNode in newCSDLinkedList])
newCSDLinkedList.deleteNode(3)
print([newNode.value for newNode in newCSDLinkedList])