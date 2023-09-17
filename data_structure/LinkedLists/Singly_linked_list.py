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


class Node:
    def __init__(self, value):
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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif self.length==0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
    
    def TraversalLinkedList(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search(self,target):
        current = self.head
        index = 1
        while current:
            if current.value==target:
                return index
            current = current.next
            index += 1
        return -1
    
    def get(self, index):
        if index == -1:
            return self.tail.value
        if index < -1 or index > self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value
    
    def set_value(self,index,value):  #Update value
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        if temp_node:
            temp_node.value = value
            return True
        return False
    
    def pop_first(self):  #remove first node and return
        if self.length==0:
            return None
        popped_node = self.head
        if self.length==1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length-=1
        return popped_node.value
    
    def pop(self):
        if self.length==0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = 1
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
        self.length-=1
        return popped_node.value

    def remove(self,index):
        prev_node = self.head
        if index ==0:
            self.head = self.head.next
            prev_node.next = None
        else:
            for _ in range(index-1):
                prev_node = prev_node.next
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
            self.length-=1

    def Delete_All(self):
        self.head = None
        self.tail = None
        self.length= 0

new_linked_list = LinkedList()
new_linked_list.prepend(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
new_linked_list.append(50)
# new_linked_list.insert(4, 60)
# print(new_linked_list)
# new_linked_list.traversal()
# print(new_linked_list.search(60))
# print(new_linked_list.get(-1))
# new_linked_list.set_value(3,100)
# print(new_linked_list.pop_first())
# print(new_linked_list.pop())
# new_linked_list.remove(4)
print(new_linked_list)  
new_linked_list.Delete_All()
print(new_linked_list)