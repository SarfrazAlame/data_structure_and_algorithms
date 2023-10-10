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
#         if self.LinkedList.head == None:
#             return True
#         else:
#             return False

#     def dequeue(self):
#         if self.isEmpty():
#             return "nothing to get"
#         else:
#             newNode = self.LinkedList.head
#             if self.LinkedList.head == self.LinkedList.tail:
#                 self.LinkedList.head = None
#                 self.LinkedList.tail = None
#             else:
#                 self.LinkedList.head = self.LinkedList.head.next
#             return newNode


# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None


# customBT = TreeNode("Drinks")
# leftChild = TreeNode("Hot")
# tea = TreeNode("tea")
# coffee = TreeNode("coffee")
# leftChild.leftChild = tea
# leftChild.rightChild = coffee
# rightChild = TreeNode("cold")
# customBT.leftChild = leftChild
# customBT.rightChild = rightChild


# ### preOrder Traversal method
# def preOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     print(rootNode.data)
#     preOrderTraversal(rootNode.leftChild)
#     preOrderTraversal(rootNode.rightChild)


# # preOrderTraversal(customBT)


# ###### inOrdertraversal method
# def inOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     inOrderTraversal(rootNode.leftChild)
#     print(rootNode.data)
#     inOrderTraversal(rootNode.rightChild)


# # inOrderTraversal(customBT)


# ######### postOrder Traversal method
# def postOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     postOrderTraversal(rootNode.leftChild)
#     postOrderTraversal(rootNode.rightChild)
#     print(rootNode.data)


# # postOrderTraversal(customBT)


# ####### Level order traversal
# def levelOrdertraversal(rootNode):
#     if not rootNode:
#         return
#     else:
#         customQueue = Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             print(root.value.data)
#             if root.value.leftChild is not None:
#                 customQueue.enqueue(root.value.leftChild)
#             if root.value.rightChild is not None:
#                 customQueue.enqueue(root.value.rightChild)


# # levelOrdertraversal(customBT)


# #####  Search method in tree  ##########
# def search(rootNode, nodeValue):
#     if not rootNode:
#         return
#     else:
#         customQueue = Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             if root.value.data == nodeValue:
#                 return "found"
#             if root.value.leftChild is not None:
#                 customQueue.enqueue(root.value.leftChild)
#             if root.value.rightChild is not None:
#                 customQueue.enqueue(root.value.rightChild)
#         return "not found"


# # print(search(customBT,'Hdot'))


# ######## insertion method ##########
# def insertion(rootNode, newNode):
#     if not rootNode:
#         return
#     else:
#         customQueue = Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             if root.value.leftChild is not None:
#                 customQueue.enqueue(root.value.leftChild)
#             else:
#                 root.value.leftChild = newNode
#                 return "the node has been successfully inserted"
#             if root.value.rightChild is not None:
#                 customQueue.enqueue(root.value.rightChild)
#             else:
#                 root.value.rightChild = newNode
#                 return "the node has been successfully inserted"


# # newNode = TreeNode("coka-cola")
# # insertion(customBT,newNode)
# # levelOrdertraversal(customBT)


# def getDeepestNode(rootNode):
#     if not rootNode:
#         return
#     else:
#         customQueue = Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             if root.value.leftChild is not None:
#                 customQueue.enqueue(root.value.leftChild)
#             if root.value.rightChild is not None:
#                 customQueue.enqueue(root.value.rightChild)
#         deepestNode = root.value
#         return deepestNode


# # deNode = getDeepestNode(customBT)
# # print(deNode.data)


# ##### delete node
# def deleteDeepestNode(rootNode, dNode):
#     if not rootNode:
#         return
#     else:
#         customQueue = Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             if root.value is dNode:
#                 root.value = None
#                 return
#             if root.value.rightChild:
#                 if root.value.rightChild is dNode:
#                     root.value.rightChild = None
#                     return
#                 else:
#                     customQueue.enqueue(root.value.rightChild)
#             if root.value.leftChild:
#                 if root.value.leftChild is dNode:
#                     root.value.leftChild = None
#                     return
#                 else:
#                     customQueue.enqueue(root.value.leftChild)


# # newNode = getDeepestNode(customBT)
# # deleteDeepestNode(customBT, newNode)
# # levelOrdertraversal(customBT)


# def deleteNodeBT(rootNode, node):
#     if not rootNode:
#         return
#     else:
#         customQueue = Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             if root.value.data == node:
#                 dNode = getDeepestNode(rootNode)
#                 root.value.data = dNode.data
#                 deleteDeepestNode(rootNode, dNode)
#                 return "node deleted"
#             if root.value.leftChild is not None:
#                 customQueue.enqueue(root.value.leftChild)
#             if root.value.rightChild is not None:
#                 customQueue.enqueue(root.value.rightChild)
#         return "failed to delete"


# # deleteNodeBT(customBT,'tea')
# # levelOrdertraversal(customBT)


# def deleteEntireNode(rootNode):
#     rootNode.data = None
#     rootNode.leftChild = None
#     rootNode.rightChild = None
#     return "deleted"


# # deleteEntireNode(customBT)
# # levelOrdertraversal(customBT)


# ###########################################    Creating Binary Tree using Python List ###########################################


# class BinaryTee:
#     def __init__(self, size):
#         self.customList = size * [None]
#         self.lastUsedIndex = 0
#         self.maxSize = size

#     def insertion(self, nodeValue):
#         if self.lastUsedIndex + 1 == self.maxSize:
#             return "the node is full"
#         self.customList[self.lastUsedIndex + 1] = nodeValue
#         self.lastUsedIndex += 1
#         return "The value has been successfully inserted"

#     def search(self, node):
#         for i in range(1, self.lastUsedIndex + 1):
#             if self.customList[i] == node:
#                 return "found"
#         return "not found"

#     def preOrderTraversal(self, index):
#         if index > self.lastUsedIndex:
#             return
#         print(self.customList[index])
#         self.preOrderTraversal(index * 2)
#         self.preOrderTraversal(index * 2 + 1)


#     def inOrderTraversal1(self, index):
#         if index > self.lastUsedIndex:
#             return
#         self.inOrderTraversal1(index * 2)
#         print(self.customList[index])
#         self.inOrderTraversal1(index * 2 + 1)

#     def postOrderTraversal1(self,index):
#         if index > self.lastUsedIndex:
#             return
#         self.postOrderTraversal1(index*2)
#         self.postOrderTraversal1(index*2+1)
#         print(self.customList[index])

#     def levelOrderTraversal(self):
#         for i in range(1,self.lastUsedIndex+1):
#             print(self.customList[i])

#     def deleteNode(self,value):
#         if self.lastUsedIndex==0:
#             return "there is not any node in the list"
#         for i in range(1,self.lastUsedIndex+1):
#             if self.customList[i]==value:
#                 self.customList[i] = self.customList[self.lastUsedIndex]
#                 self.customList[self.lastUsedIndex]=None
#                 self.lastUsedIndex-=1
#                 return "node deleted"

#     def deleteEntireNode(self):
#         self.customList = None
#         return "entire deleted"

# newBT = BinaryTee(8)
# newBT.insertion("Drinks")
# newBT.insertion("Hot")
# newBT.insertion("Cold")
# newBT.insertion("tea")
# newBT.insertion("coffee")
# print(newBT.customList)
# print(newBT.search("tea"))
# newBT.preOrderTraversal(1)
# newBT.inOrderTraversal1(1)
# newBT.postOrderTraversal1(1)
# newBT.levelOrderTraversal()
# newBT.deleteNode('tea')
# newBT.deleteNode('Drinks')
# newBT.levelOrderTraversal()
# newBT.deleteEntireNode()


############################   again practice using linked list  ###############################


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = TreeNode("drinks")
leftChild = TreeNode("hot")
rightChild = TreeNode("cold")
tea = TreeNode("tea")
coffee = TreeNode("coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
newBT.leftChild = leftChild
newBT.rightChild = rightChild


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


# preOrderTraversal(newBT)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


# inOrderTraversal(newBT)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


# postOrderTraversal(newBT)


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
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.LinkedList]
        return " ".join(values)

    def enqueue(self, value):
        newNode = Node(value)
        if self.LinkedList.head == None:
            self.LinkedList.head = newNode
            self.LinkedList.tail = newNode
        else:
            self.LinkedList.tail.next = newNode
            self.LinkedList.tail = newNode

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.LinkedList.head == None:
            return "nothing to remove"
        else:
            headNode = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
        return headNode


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)


# levelOrderTraversal(newBT)


def search(rootNode, nodeValue):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "found"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "not found"


# print(search(newBT,'Tea'))


def insertion(rootNode, newNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "node has been successfully inserted"
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "node has been successfully inserted"


# newNode1 = TreeNode("coka-cola")
# newNode2 = TreeNode("pepsi")
# insertion(newBT,newNode1)
# insertion(newBT,newNode2)
# levelOrderTraversal(newBT)


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return root.value


# dNode = getDeepestNode(newBT)
# print(dNode.data)


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return None
                else:
                    customQueue.enqueue(root.value.rightChild)


# dNode = getDeepestNode(newBT)
# deleteDeepestNode(newBT,dNode)
# levelOrderTraversal(newBT)


def deleteNode(rootNode, node):
    if not rootNode:
        return
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(newBT)
                root.value.data = dNode.data
                deleteDeepestNode(newBT, dNode)
                return "node deleted successfully"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "fail to delete"


# deleteNode(newBT,'drinks')
# levelOrderTraversal(newBT)


def deleteEntireBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "deleted "


# print(deleteEntireBT(newBT))
# levelOrderTraversal(newBT)


# ###########################################    Creating Binary Tree using Python List ###########################################
class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertion(self, nodeValue):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "list is full"
        self.customList[self.lastUsedIndex + 1] = nodeValue
        self.lastUsedIndex += 1
        return "element inserted successfully"

    def Search(self, element):
        for i in range(0, self.lastUsedIndex + 1):
            if self.customList[i] == element:
                return "found"
        return "not found"

    def preOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)

    def inOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index * 2)
        print(self.customList[index])
        self.inOrderTraversal(index * 2 + 1)

    def postOrderTraversal(self, index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.customList[index])

    def levelOrderTraversal(self):
        for i in range(1, self.lastUsedIndex + 1):
            print(self.customList[i])

    def deleteNodeBT(self, nodeValue):
        if self.lastUsedIndex == 0:
            return "nothing to delete"
        else:
            for i in range(1, self.lastUsedIndex + 1):
                if self.customList[i] == nodeValue:
                    self.customList[i] = self.customList[self.lastUsedIndex]
                    self.customList[self.lastUsedIndex] = None
                    self.lastUsedIndex -= 1
                    return "node deleted"
    
    def deleteEntireList(self):
        self.customList = None
        return "deleted"


customBT = BinaryTree(8)
customBT.insertion("drinks")
customBT.insertion("hot")
customBT.insertion("cold")
customBT.insertion("tea")
customBT.insertion("coffee")
# customBT.preOrderTraversal(1)
# customBT.inOrderTraversal(1)
# customBT.postOrderTraversal(1)
# customBT.levelOrderTraversal()
# customBT.deleteNodeBT('hot')
# print(customBT.customList)
# customBT.levelOrderTraversal()
# customBT.deleteEntireList()
# print(customBT.customList)