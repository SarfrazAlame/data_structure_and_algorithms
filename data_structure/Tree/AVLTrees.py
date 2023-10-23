import QueueLinkedList as queue


# class AVLTree:
#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None
#         self.height = 1


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


# def SearchNode(rootNode, nodeValue):
#     if rootNode.data == nodeValue:
#         print("the value is found")
#     elif nodeValue < rootNode.data:
#         if rootNode.leftChild.data == nodeValue:
#             return "found"
#         else:
#             SearchNode(rootNode.leftChild, nodeValue)
#     else:
#         if rootNode.rightChild == nodeValue:
#             return "found"
#         else:
#             SearchNode(rootNode.rightChild, nodeValue)


# def getHeight(rootNode):
#     if not rootNode:
#         return 0
#     return rootNode.height


# def rightRotate(disbalancedNode):
#     newRoot = disbalancedNode.leftChild
#     disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
#     newRoot.rightChild = disbalancedNode
#     disbalancedNode.height = 1 + max(
#         getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild)
#     )
#     newRoot.height = 1 + max(
#         getHeight(newRoot.leftChild), getHeight(newRoot.rightChild)
#     )
#     return newRoot


# def leftRotate(disbalancedNode):
#     newRoot = disbalancedNode.rightChild
#     disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
#     newRoot.leftChild = disbalancedNode
#     disbalancedNode.height = 1 + max(
#         getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild)
#     )
#     newRoot.height = 1 + max(
#         getHeight(newRoot.leftChild), getHeight(newRoot.rightChild)
#     )
#     return newRoot


# def getBalance(rootNode):
#     if not rootNode:
#         return 0
#     return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


# def insertNode(rootNode, nodeValue):
#     if not rootNode:
#         return AVLTree(nodeValue)
#     elif nodeValue < rootNode.data:
#         rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
#     else:
#         rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)

#     rootNode.height = 1 + max(
#         getHeight(rootNode.rightChild), getHeight(rootNode.leftChild)
#     )
#     balance = getBalance(rootNode)

#     if balance > 1 and nodeValue < rootNode.leftChild.data:
#         return rightRotate(rootNode)
#     if balance > 1 and nodeValue > rootNode.leftChild.data:
#         rootNode.leftChild = leftRotate(rootNode.leftChild)
#         return rightRotate(rootNode)
#     if balance < -1 and nodeValue > rootNode.rightChild.data:
#         return leftRotate(rootNode)
#     if balance < -1 and nodeValue < rootNode.rightChild.data:
#         rootNode.rightChild = rightRotate(rootNode.rightChild)
#         leftRotate(rootNode)
#     return rootNode


# def getMinValueNode(rootNode):
#     if rootNode is None or rootNode.leftChild is None:
#         return rootNode
#     return getMinValueNode(rootNode.leftChild)


# def deleteNode(rootNode, nodeValue):
#     if not rootNode:
#         return rootNode
#     elif nodeValue < rootNode.data:
#         rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
#     elif nodeValue > rootNode.data:
#         rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
#     else:
#         if rootNode.leftChild is None:
#             temp = rootNode.rightChild
#             rootNode = None
#             return temp
#         elif rootNode.rightChild is None:
#             temp = rootNode.leftChild
#             rootNode = None
#             return temp
#         temp = getMinValueNode(rootNode.rightChild)
#         rootNode.data = temp.data
#         rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

#     balance = getBalance(rootNode)
#     if balance > 1 and getBalance(rootNode.leftChild) >= 0:
#         return rightRotate(rootNode)
#     if balance < -1 and getBalance(rootNode.rightChild) <= 0:
#         return leftRotate(rootNode)
#     if balance > 1 and getBalance(rootNode.leftChild) < 0:
#         rootNode.leftChild = leftRotate(rootNode.leftChild)
#         return rightRotate(rootNode)
#     if balance < -1 and getBalance(rootNode.rightChild) > 0:
#         rootNode.rightChild = rightRotate(rootNode.rightChild)
#         return leftRotate(rootNode)

#     return rootNode


# def deleteEntireTree(rootNode):
#     rootNode.data = None
#     rootNode.leftChild = None
#     rootNode.rightChild = None


# newAVL = AVLTree(5)
# newAVL = insertNode(newAVL, 10)
# newAVL = insertNode(newAVL, 15)
# newAVL = insertNode(newAVL, 20)
# newAVL = insertNode(newAVL, 25)
# # print(SearchNode(newAVL,10))
# # deleteNode(newAVL,20)
# deleteEntireTree(newAVL)
# levelOrderTraversal(newAVL)


##################################### Practice AVLTrees  #####################################


class AVLTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
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
    if nodeValue == rootNode.data:
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


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(
        getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild)
    )
    newRoot.height = 1 + max(
        getHeight(newRoot.leftChild), getHeight(newRoot.rightChild)
    )
    return newRoot


def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(
        getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild)
    )
    newRoot.height = 1 + max(
        getHeight(newRoot.leftChild), getHeight(newRoot.rightChild)
    )
    return newRoot


def getBalanced(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def inserteNode(rootNode, nodeValue):
    if not rootNode:
        return AVLTree(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = inserteNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = inserteNode(rootNode.rightChild, nodeValue)

    rootNode.height = 1 + max(
        getHeight(rootNode.rightChild), getHeight(rootNode.leftChild)
    )

    balanced = getBalanced(rootNode)

    if balanced > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balanced > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balanced < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balanced < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode

def getMinNodeValue(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    else:
        getMinNodeValue(rootNode.leftChild)

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = getMinNodeValue(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

    balance = getBalanced(rootNode)
    if balance > 1 and getBalanced(rootNode.leftChild) >= 0:
        return rightRotate(rootNode)
    if balance < -1 and getBalanced(rootNode.rightChild) <= 0:
        return leftRotate(rootNode)
    if balance > 1 and getBalanced(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and getBalanced(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)

    return rootNode

def deleteAllNode(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None


newAVL = AVLTree(5)
newAVL = inserteNode(newAVL,10)
newAVL = inserteNode(newAVL,15)
newAVL = inserteNode(newAVL,20)
# deleteNode(newAVL,5)
# deleteAllNode(newAVL)
levelOrderTraversal(newAVL)