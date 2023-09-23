class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"Person is {self.name} and age is {self.age}"

new_person = Person("Sarfraz",21)
print(new_person)


# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# class AddLinkedList:
#     def __init__(self,data):
#         new_node = Node(data)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

# new_lindked_list = AddLinkedList(12)
# print(new_lindked_list.tail.data)
# print(new_lindked_list.head.data)


# //////////////////////insertion in linked list


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.head.next = new_node
#             self.tail = new_node

#     def __str__(self):
#         temp_node = self.head
#         result = ""
#         while temp_node is not None:
#             result += str(temp_node.value)
#             if temp_node.next is not None:
#                 result += "->"
#             temp_node = temp_node.next
#         return result

# new_linked_list = LinkedList()
# new_linked_list.append(10)
# new_linked_list.append(15)
# new_linked_list.append(20)
# print(new_linked_list)


# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self,data):
#         new_node = Node(data)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1

# new_linked_list = LinkedList(10)
# print(new_linked_list.tail.value)


# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

#     def append(self,value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.head.next = new_node
#             self.tail = new_node

#     def __str__(self):
#         temp_node = self.head
#         result = ""
#         while temp_node is not None:
#             result += str(temp_node.value)
#             if temp_node.next is not None:
#                 result += "-->"
#             temp_node = temp_node.next
#         return result

# new_linked_lists = LinkedList()
# new_linked_lists.append(12)
# new_linked_lists.append(10)
# new_linked_lists.append(30)
# print(new_linked_lists)


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def __str__(self):
#         current = self.head
#         elements = []
#         while current:
#             elements.append(str(current.data))
#             current = current.next
#         return " -> ".join(elements)

# # Usage example:
# my_linked_list = LinkedList()
# my_linked_list.head = Node(1)
# my_linked_list.head.next = Node(2)
# my_linked_list.head.next.next = Node(3)
# my_linked_list.head.next.next.next = Node(4)

# print(my_linked_list)


# ##################  Append, Prepend, Traversal, insert and search in LinkedList
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
#         elif self.length == 0:
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
#         return True

#     def traversal(self):
#         current = self.head
#         while current:
#             print(current.value)
#             current = current.next

#     def search(self, target):
#         current = self.head
#         while current:
#             if current.value == target:
#                 return True
#             current = current.next
#         return False

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
    
#     def pop_first(self):  #remove first node and remove
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



# new_linked_list = LinkedList()
# new_linked_list.prepend(10)
# new_linked_list.append(20)
# new_linked_list.append(30)
# new_linked_list.append(40)
# new_linked_list.append(50)
# # new_linked_list.insert(4, 60)
# print(new_linked_list)
# # new_linked_list.traversal()
# # print(new_linked_list.search(60))
# # print(new_linked_list.get(-1))
# # new_linked_list.set_value(3,100)
# # print(new_linked_list.pop_first())
# print(new_linked_list.pop())
# print(new_linked_list)  




############################## Practice once again
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
     
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += "->"
            temp_node = temp_node.next
        return result

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node 
        self.length+=1
    
    def insert(self,index,value):
        new_node = Node(value)
        if index <0 or index > self.length:
            return None
        elif self.length == 0:
            self.head = value
            self.tail = value
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length+=1
        
    def traversal(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search(self,target):
        current = self.head
        while current:
            if current.value==target:
                return True
            current = current.next
        return False
    
    def get(self,index):
        if index < 0 or index >self.length:
            return None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current.value
    
    def set_value(self,index,value):
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        temp_node.next = value
        
        


new_linked_list = LinkedList()
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.prepend(10)
new_linked_list.insert(3,40)
print(new_linked_list)
# new_linked_list.traversal()
# print(new_linked_list.search(20))
# print(new_linked_list.get(2))