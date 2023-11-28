# class Queue:
#     def __init__(self):
#         self.items = []

#     def __str__(self):
#         values = [str(x) for x in self.items]
#         return " ".join(values)

#     def isEmpty(self):
#         if self.items == []:
#             return True
#         else:
#             return False

#     def enqueue(self, value):
#         self.items.append(value)
#         return "element inserted successfully"

#     def dequeue(self):
#         if self.isEmpty():
#             return "There is not any element to remove"
#         else:
#             return self.items.pop(0)

#     def peek(self):
#         if self.isEmpty():
#             return "There is not any element to remove"
#         else:
#             return self.items[0]

#     def delete(self):
#         self.items = None


# customQueue = Queue()
# # print(customQueue.isEmpty())
# customQueue.enqueue(10)
# customQueue.enqueue(20)
# customQueue.enqueue(30)
# customQueue.enqueue(40)
# # print(customQueue)
# # print(customQueue.dequeue())
# print(customQueue.peek())
# customQueue.delete()


###########################   Queue using Linked list  ##########################################

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

#     def __str__(self):
#         return str(self.value)

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def __iter__(self):
#         curNode = self.head
#         while curNode:
#             yield curNode
#             curNode = curNode.next


# class Queue:
#     def __init__(self):
#         self.LinkedList = LinkedList()

#     def __str__(self):
#         values = [str(x) for x in self.LinkedList]
#         return " ".join(values)

#     def enqueue(self, value):
#         newNode = Node(value)
#         if self.LinkedList.head == None:
#             self.LinkedList.head = newNode
#             self.LinkedList.tail = newNode
#         else:
#             self.LinkedList.tail.next = newNode
#             self.LinkedList.tail = newNode

#     def isEmpty(self):
#         if self.LinkedList.head==None:
#             return True
#         else:
#             return False

#     def dequeue(self):
#         if self.isEmpty():
#             return "There is not any node in the Queue"
#         else:
#             tempNode = self.LinkedList.head
#             if self.LinkedList.head==self.LinkedList.tail:
#                 self.LinkedList.head=None
#                 self.LinkedList.tail=None
#             else:
#                 self.LinkedList.head = self.LinkedList.head.next
#             return tempNode

#     def peek(self):
#         if self.isEmpty():
#             return "there's not any element to get"
#         else:
#             return self.LinkedList.head

#     def delete(self):
#         self.LinkedList.head=None
#         self.LinkedList.tail=None

# customQueue = Queue()
# customQueue.enqueue(12)
# customQueue.enqueue(14)
# customQueue.enqueue(16)
# # print(customQueue)
# # print(customQueue.dequeue())
# print(customQueue.peek())


####################################  Python Collection Module  ##############################

# from collections import deque

# customQueue = deque(maxlen=3)

# customQueue.append(10)
# customQueue.append(20)
# customQueue.append(30)
# customQueue.append(30)

# print(customQueue)
# # print(customQueue.popleft())
# customQueue.clear()
# print(customQueue)


####################################  Python Queue Module  ##############################

# import queue as q

# customQueue = q.Queue(maxsize=3)
# customQueue.put(1)
# customQueue.put(2)
# customQueue.put(3)
# print(customQueue.qsize())


###########################################  Practice Queue    #################################

# class Queue:
#     def __init__(self):
#         self.items = []

#     def __str__(self):
#         values = [str(x) for x in self.items]
#         return " ".join(values)

#     def isEmpty(self):
#         if self.items==[]:
#             return True
#         else:
#             return False

#     def enqueue(self,value):
#         self.items.append(value)
#         return "element appended successfully"

#     def dequeue(self):
#         if self.isEmpty():
#             return 'nothing to delete'
#         self.items.pop(0)

#     def peek(self):
#         if self.isEmpty():
#             return "there is not any element to remove"
#         return self.items[0]

#     def delete(self):
#         self.items = None


# customQueue = Queue()
# # print(customQueue.isEmpty())
# customQueue.enqueue(10)
# customQueue.enqueue(20)
# customQueue.enqueue(30)
# customQueue.enqueue(40)
# customQueue.enqueue(50)
# # print(customQueue)
# customQueue.dequeue()
# customQueue.delete()
# # print(customQueue)
# # print(customQueue.peek())


###########################################  Practice Queue using Linked List   #################################

# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

#     def __str__(self):
#         return str(self.value)

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def __iter__(self):
#         curNode = self.head
#         while curNode:
#             yield curNode
#             curNode = curNode.next

# class Queue:
#     def __init__(self):
#         self.LinkedList = LinkedList()

#     def __str__(self):
#         values = [str(x) for x in self.LinkedList]
#         return ' '.join(values)

#     def enqueue(self,value):
#         newNode = Node(value)
#         if self.LinkedList.head==None:
#             self.LinkedList.head = newNode
#             self.LinkedList.tail = newNode
#         else:
#             self.LinkedList.tail.next = newNode
#             self.LinkedList.tail = newNode

#     def isEmpty(self):
#         if self.LinkedList.head==None:
#             return True
#         else:
#             return False

#     def dequeue(self):
#         if self.LinkedList.head==None:
#             return "there is not any element to delete"
#         else:
#            tempNode = self.LinkedList.head
#            if self.LinkedList.head == self.LinkedList.tail:
#                self.LinkedList.head = None
#                self.LinkedList.tail = None
#            else:
#                self.LinkedList.head  = self.LinkedList.head.next
#            return tempNode

#     def peek(self):
#         if self.LinkedList.head==None:
#             return "there is not any element to show"
#         else:
#             return self.LinkedList.head

#     def delete(self):
#         self.LinkedList.head=None
#         self.LinkedList.tail = None

# customQueue = Queue()
# customQueue.enqueue(10)
# customQueue.enqueue(20)
# customQueue.enqueue(30)
# customQueue.enqueue(40)
# # print(customQueue.isEmpty())
# customQueue.dequeue()
# # print(customQueue.peek())
# customQueue.delete()
# print(customQueue)


###############################  practice Queue  #############################


# class Queue:
#     def __init__(self):
#         self.items = []

#     def __str__(self):
#         values = [str(x) for x in self.items]
#         return " ".join(values)

#     def isEmpty(self):
#         if self.items == []:
#             return True
#         return False

#     def enqueue(self, value):
#         self.items.append(value)
#         return "item has successfully been inserted"

#     def dequeue(self):
#         if self.isEmpty():
#             return "nothing to remove"
#         else:
#             return self.items.pop(0)

#     def peek(self):
#         if self.isEmpty():
#             return "nothign to show"
#         else:
#             return self.items[0]

#     def delete(self):
#         self.items = None


# customQueue = Queue()
# customQueue.enqueue(12)
# customQueue.enqueue(15)
# customQueue.enqueue(10)
# customQueue.enqueue(23)
# # print(customQueue.isEmpty())
# # print(customQueue.dequeue())
# # print(customQueue.dequeue())
# customQueue.delete()
# print(customQueue)


#########################  Queue using LinkedList ################
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        tempNode = self.head
        while tempNode:
            yield tempNode
            tempNode = tempNode.next


class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.LinkedList]
        return " ".join(values)

    def enqueue(self, value):
        newNode = Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        return False

    def dequeue(self):
        if self.isEmpty():
            return "nothing to delete"
        else:
            tempNode = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
            return tempNode
        
    def peek(self):
        if self.LinkedList.head is None:
            return "nothing to delete"
        else:
            return self.LinkedList.head
    
    def delete(self):
        self.LinkedList.head = None
        

customQueue = Queue()
# print(customQueue.isEmpty())
customQueue.enqueue(12)
customQueue.enqueue(10)
customQueue.enqueue(15)
customQueue.enqueue(23)
# print(customQueue.dequeue())
# print(customQueue.peek())
customQueue.delete()
print(customQueue)
