import QueueLinkedList as queue

# class BSTNode():
#     def __init__(self,data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None

# def insertNode(rootNode,nodeValue):
#     if rootNode.data == None:
#         rootNode.data = nodeValue
#     elif nodeValue <= rootNode.data:
#         if rootNode.leftChild is None:
#             rootNode.leftChild = BSTNode(nodeValue)
#         else:
#             insertNode(rootNode.leftChild,nodeValue)
#     else:
#         if rootNode.rightChild is None:
#             rootNode.rightChild = BSTNode(nodeValue)
#         else:
#             insertNode(rootNode.rightChild,nodeValue)
#     return "The node has been successfully inserted"

# def preOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     print(rootNode.data)
#     preOrderTraversal(rootNode.leftChild)
#     preOrderTraversal(rootNode.rightChild)

# def inOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     inOrderTraversal(rootNode.leftChild)
#     print(rootNode.data)
#     inOrderTraversal(rootNode.rightChild)

# def postOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     postOrderTraversal(rootNode.leftChild)
#     postOrderTraversal(rootNode.rightChild)
#     print(rootNode.data)

# def levelOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     else:
#         customQueue = queue.Queue()
#         customQueue.enqueue(rootNode)
#         while not customQueue.isEmpty():
#             root = customQueue.dequeue()
#             print(root.value.data)
#             if root.value.leftChild is not None:
#                 customQueue.enqueue(root.value.leftChild)
#             if root.value.rightChild is not None:
#                 customQueue.enqueue(root.value.rightChild)

# def search(rootNode,nodeValue):
#     if rootNode.data == nodeValue:
#        print("found")
#     elif nodeValue < rootNode.data:
#         if rootNode.leftChild.data == nodeValue:
#            print("found")
#         else:
#             search(rootNode.leftChild, nodeValue)
#     else:
#         if rootNode.rightChild.data == nodeValue:
#            print("found")
#         else:
#             search(rootNode.rightChild, nodeValue)

# def minValueNode(bstNode):
#     current = bstNode
#     while (current.leftChild is not None):
#         current = current.leftChild
#     return current

# def deleteNode(rootNode,nodeValue):
#     if rootNode is None:
#         return rootNode
#     if nodeValue < rootNode.data:
#         rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue)
#     elif nodeValue > rootNode.data:
#         rootNode.rightChild = deleteNode(rootNode.rightChild,nodeValue)
#     else:
#         if rootNode.leftChild is None:
#             temp = rootNode.rightChild
#             rootNode = None
#             return temp
#         if rootNode.rightChild is None:
#             temp = rootNode.leftChild
#             rootNode = None
#             return temp

#         temp = minValueNode(rootNode.rightChild)
#         rootNode.data = temp.data
#         rootNode.rightChild = deleteNode(rootNode.rightChild,temp.data)
#     return rootNode

# def deleteBST(rootNode):
#     rootNode.data = None
#     rootNode.leftChild = None
#     rootNode.rightChild = None
#     return "The BST has been successfully deleted"


# newBST = BSTNode(None)
# insertNode(newBST,70)
# insertNode(newBST,60)
# insertNode(newBST,80)
# insertNode(newBST,10)
# insertNode(newBST,100)
# insertNode(newBST,20)
# insertNode(newBST,28)
# insertNode(newBST,40)
# preOrderTraversal(newBST)
# print(newBST.leftChild)
# inOrderTraversal(newBST)
# postOrderTraversal(newBST)
# levelOrderTraversal(newBST)
# search(newBST,10)
# deleteNode(newBST,100)
# deleteNode(newBST,70)
# deleteBST(newBST)
# levelOrderTraversal(newBST)


#####################################################  Practice  Binary Search Tree  #####################################################


# class BSTNode:
#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None


# def insertNode(rootNode, nodeValue):
#     if rootNode.data == None:
#         rootNode.data = nodeValue
#     elif nodeValue <= rootNode.data:
#         if rootNode.leftChild is None:
#             rootNode.leftChild = BSTNode(nodeValue)
#         else:
#             insertNode(rootNode.leftChild, nodeValue)
#     else:
#         if rootNode.rightChild is None:
#             rootNode.rightChild = BSTNode(nodeValue)
#         else:
#             insertNode(rootNode.rightChild, nodeValue)
#     return "The node has been successfully inserted"


# def preOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     print(rootNode.data)
#     preOrderTraversal(rootNode.leftChild)
#     preOrderTraversal(rootNode.rightChild)


# def inOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     inOrderTraversal(rootNode.leftChild)
#     print(rootNode.data)
#     inOrderTraversal(rootNode.rightChild)


# def postOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     postOrderTraversal(rootNode.leftChild)
#     postOrderTraversal(rootNode.rightChild)
#     print(rootNode.data)


# def levelOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     else:
#         customQueue = queue.Queue()
#         customQueue.enqueue(rootNode)
#         while not customQueue.isEmpty():
#             root = customQueue.dequeue()
#             print(root.value.data)
#             if root.value.leftChild is not None:
#                 customQueue.enqueue(root.value.leftChild)
#             if root.value.rightChild is not None:
#                 customQueue.enqueue(root.value.rightChild)


# def Search(rootNode, nodeValue):
#     if rootNode.data == nodeValue:
#         print("found")
#     elif nodeValue < rootNode.data:
#         if rootNode.leftChild.data == nodeValue:
#             print("found")
#         else:
#             Search(rootNode.leftChild, nodeValue)
#     else:
#         if rootNode.rightChild.data == nodeValue:
#             print("found")
#         else:
#             Search(rootNode.rightChild, nodeValue)


# def getMinValue(bstNode):
#     current = bstNode
#     while current.leftChild is not None:
#         current = current.leftChild
#     return current


# def deleteNode(rootNode, nodeValue):
#     if rootNode is None:
#         return rootNode
#     if nodeValue < rootNode.data:
#         rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
#     elif nodeValue > rootNode.data:
#         rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
#     else:
#         if rootNode.leftChild is None:
#             temp = rootNode.rightChild
#             rootNode = None
#             return temp
#         if rootNode.rightChild is None:
#             temp = rootNode.leftChild
#             rootNode = None
#             return temp

#         temp = getMinValue(rootNode.rightChild)
#         rootNode.data = temp.data
#         rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
#     return rootNode

# def deleteEntireNode(rootNode):
#     rootNode.data = None
#     rootNode.leftChild =None
#     rootNode.rightChild = None


# newBST = BSTNode(None)
# insertNode(newBST, 20)
# insertNode(newBST, 15)
# insertNode(newBST, 50)
# insertNode(newBST, 30)
# insertNode(newBST, 25)
# insertNode(newBST, 45)
# insertNode(newBST, 23)
# insertNode(newBST, 68)
# # preOrderTraversal(newBST)
# # inOrderTraversal(newBST)
# # levelOrderTraversal(newBST)
# # Search(newBST, 20)
# # deleteNode(newBST, 20)
# deleteEntireNode(newBST)
# levelOrderTraversal(newBST)


#####################################################  Practice once again Binary Search Tree  #####################################################


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "node has been successfully inserted"


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    preOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)


def Search(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("found")
        else:
            Search(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("found")
        else:
            Search(rootNode.rightChild, nodeValue)


def getMinNode(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild
    return current

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        temp = getMinNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode


newBST = BSTNode(None)
insertNode(newBST, 10)
insertNode(newBST, 15)
insertNode(newBST, 5)
insertNode(newBST, 50)
insertNode(newBST, 34)
insertNode(newBST, 98)
insertNode(newBST, 76)
# preOrderTraversal(newBST)
# inOrderTraversal(newBST)
# postOrderTraversal(newBST)
# levelOrderTraversal(newBST)
# Search(newBST,716)
deleteNode(newBST, 10)
levelOrderTraversal(newBST)