class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CSLinkedList:
    # def __init__(self,value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += "->"
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def preppend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insertion(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return None
        elif self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        elif index == 0:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.length += 1

    def traversal(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
            if current == self.head:
                break

    def search(self, target):
        current = self.head
        while current:
            if current.value == target:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def set_value(self, index, value):
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        if temp_node:
            temp_node.value = value

    def pop_first(self):
        currrent = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = currrent.next
            self.tail.next = currrent.next
            currrent.next = None
            self.length -= 1
        return currrent.value
    
    def pop(self):
        popped_node = self.tail
        temp_node = self.head
        if self.length == 0:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
        else:
            while temp_node is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next=self.head
            popped_node.next = None
        self.length-=1
        return popped_node.value
    
    def remove(self,index):
        prev_element = self.head
        if index == 0:
            self.head = prev_element.next
            self.tail.next = prev_element.next
            prev_element.next = None
        else:
            for _ in range(index-1):
                prev_element=prev_element.next
            removed_node = prev_element.next
            prev_element.next = removed_node.next
            removed_node.next = None
            self.length-=1
        
     
    def delete_all(self):
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0


cslinkedList = CSLinkedList()
cslinkedList.append(10)
cslinkedList.append(20)
cslinkedList.append(30)
cslinkedList.append(40)
cslinkedList.preppend(60)
cslinkedList.insertion(5, 200)
print(cslinkedList)
# cslinkedList.traversal()
# print(cslinkedList.search(202))
# print(cslinkedList.get(1))
# cslinkedList.set_value(5,100)
# print(cslinkedList.pop_first())
# print(cslinkedList.pop())
# cslinkedList.remove(0)
cslinkedList.delete_all()
print(cslinkedList)