# class Node:
#     def __init__(self, value=None):
#         self.value = value
#         self.next = None
#         self.prev = None


# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def __iter__(self):
#         node = self.head
#         while node:
#             yield node
#             node = node.next

#     # creation of doubly linked lists
#     def createDLL(self, nodeValue):
#         node = Node(nodeValue)
#         self.head = node
#         self.tail = node
#         node.prev = None
#         node.next = None
#         return "DLL is created successfully"

#     # Insertion method in doubly linked list
#     def insertNode(self, nodeValue, location):
#         if self.head is None:
#             print("the node cannot be inserted")
#         else:
#             newNode = Node(nodeValue)
#             if location == 0:
#                 newNode.prev = None
#                 newNode.next = self.head
#                 self.head.prev = newNode
#                 self.head = newNode
#             elif location == 1:
#                 newNode.next = None
#                 newNode.prev = self.tail
#                 self.tail.next = newNode
#                 self.tail = newNode
#             else:
#                 tempNode = self.head
#                 index = 0
#                 while index < location - 1:
#                     tempNode = tempNode.next
#                     index += 1
#                 newNode.next = tempNode.next
#                 newNode.prev = tempNode
#                 newNode.next.prev = newNode
#                 tempNode.next = newNode

#     #  Traversal Method in Doubly Linked List
#     def traversalDLL(self):
#         if self.head is None:
#             print("There is not any element to tarverse")
#         else:
#             temp_node = self.head
#             while temp_node:
#                 print(temp_node.value)
#                 temp_node = temp_node.next

#    # Reverse Taversal in Doubly Linked List
#     def ReverseTravesalDLL(self):
#         if self.head is None:
#             print("there is not any element to reverse traverse")
#         else:
#             tempNode = self.tail
#             while tempNode:
#                 print(tempNode.value)
#                 tempNode = tempNode.prev

#     # Searching for the node in the doubly Linked List
#     def SearchDLL(self,target):
#         if self.head is None:
#             return "there is not any element to search"
#         else:
#             temp_node = self.head
#             while temp_node:
#                 if temp_node.value == target:
#                     return True
#                 temp_node = temp_node.next
#             return False

#     # Deletion in doublly linked list
#     def Deletion(self,location):
#         if self.head is None:
#             print("nothing to delete")
#         else:
#             if location==0:
#                 if self.head==self.tail:
#                     self.head = None
#                     self.tail = None
#                 else:
#                     self.head.next = self.head
#                     self.head.prev = None
#             elif location==1:
#                 if self.head == self.tail:
#                     self.head=None
#                     self.tail=None
#                 else:
#                     self.tail = self.tail.prev
#                     self.tail.next = None
#             else:
#                 tempNode = self.head
#                 for _ in range(location-1):
#                     tempNode = tempNode.next
#                 tempNode.next = tempNode.next.next
#                 tempNode.next.prev = tempNode
#             print("the node has been successfully deleted")


#     # Delete Entire Doubly Linked List
#     def DeleteAllNode(self):
#         if self.head is None:
#             print("nothing to delete")
#         else:
#             tempNode = self.head
#             while tempNode:
#                 tempNode.prev = None
#                 tempNode = tempNode.next
#             self.head = None
#             self.tail = None


# doublyLL = DoublyLinkedList()
# doublyLL.createDLL(30)
# doublyLL.insertNode(20,0)
# doublyLL.insertNode(10,1)
# doublyLL.insertNode(40,2)
# doublyLL.insertNode(50,3)
# print([node.value for node in doublyLL])
# # doublyLL.traversalDLL()
# # print("   ")
# # doublyLL.ReverseTravesalDLL()
# # print(doublyLL.SearchDLL(30))
# # doublyLL.Deletion(-1)
# doublyLL.DeleteAllNode()
# print([node.value for node in doublyLL])


################################# practice DoublyLinkedList ################################


class Node:
    def __init__(self, value=None):
        self.value = value
        self.pre = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createNode(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.pre = None
        newNode.next = None
        return "node inserted successfully"

    def insertNode(self, location, value):
        newNode = Node(value)
        if self.head is None:
            print("node can't be inserted")
        else:
            if location == 0:
                newNode.pre = None
                newNode.next = self.head
                self.head.pre = newNode
                self.head = newNode
            else:
                preNode = self.head
                index = 0
                while index < location - 1:
                    preNode = preNode.next
                    index += 1
                newNode.next = preNode.next
                preNode.next = newNode
                newNode.pre = preNode
                newNode.next.pre = newNode

    def TraverseNode(self):
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.next

    def ReverseTraversal(self):
        tempNode = self.tail
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.pre

    def SearchNode(self, target):
        tempNode = self.head
        while tempNode:
            if tempNode.value == target:
                return True
            tempNode = tempNode.next
        return False
    
    def deleteNode(self,location):
        tempNode = self.head
        if location == 0:
            if self.head==self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = tempNode.next
                tempNode.next = None

        else:
            tempNode = self.head
            for _ in range(location-1):
                tempNode = tempNode.next
            removedNode = tempNode.next
            tempNode.next = removedNode.next
            removedNode.next.pre = tempNode
            removedNode.pre = None
            removedNode.next = None
    
    def deleteAllNode(self):
        tempNode = self.head
        while tempNode:
            tempNode.pre = None
            tempNode = tempNode.next
        self.head = None
        self.tail = None




doublyLL = DoublyLinkedList()
doublyLL.createNode(12)
doublyLL.insertNode(0, 10)
doublyLL.insertNode(1, 16)
doublyLL.insertNode(2, 24)
# doublyLL.TraverseNode()
# doublyLL.ReverseTraversal()
# print(doublyLL.SearchNode(24))
print([node.value for node in doublyLL])
# doublyLL.deleteNode(0)
doublyLL.deleteAllNode()
print([node.value for node in doublyLL])
