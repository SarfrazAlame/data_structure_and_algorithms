# Binary trees are the data structures in which each node has at most two children, aften referred to as the left and right children

############################  types of Binary Tree ##################

# 1. full Binary Tree :  if each node of a binary tree  has a zero or two children but not one called full binary tree
# 2. Perfect Binary Tree: all none leaf node has two children called Perfect Binary Tree
# 3. Complete Binary Tree: all node has full trees
# 4. Balanced Binary Tree:  each leaf is not more than a certain distance from the root node than any other leaf

#   in binary form

# letf child = cell[2x]
# Right child = cell[2x+1]


###########################  creating binary tree using linked list   #################
# 1. Creation of Tree
# 2.Insertion of a node
# 3. Deletion of a node
# 4. Search for a value
# 5. Traversal all node
# 6. Deletion of tree


# class TreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None

# newBT = TreeNode("Drinks")

##################################### Traversal of Binary Tree  ####################################

# 1.Depth first search
#   - Preorder traversal :  Root Node - left Subtree - Right Subtree
#   - Inorder traversal  : left Subtree - Root Node - Right Subtree
#   - Post order traversal: left Subtree - Right Subtree - Root Node

# 2. Breadth first search
#   - Level order traversal

# preorder traversal
# import QueueLinkedList as queue


# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.leftChild = None
#         self.rightChild = None


# newBT = TreeNode("Drinks")
# leftChild = TreeNode("Hot")
# tea = TreeNode("Tea")
# coffee = TreeNode("coffee")
# leftChild.leftChild = tea
# leftChild.rightChild = coffee
# rightChild = TreeNode("Cold")
# newBT.leftChild = leftChild
# newBT.rightChild = rightChild


# # preorder traversal method
# def preOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     print(rootNode.data)
#     preOrderTraversal(rootNode.leftChild)
#     preOrderTraversal(rootNode.rightChild)

# # preOrderTraversal(newBT)

# ####### Inorder traversal method
# def inOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     inOrderTraversal(rootNode.leftChild)
#     print(rootNode.data)
#     inOrderTraversal(rootNode.rightChild)


# # inOrderTraversal(newBT)


# ####### postOrdertraversal method
# def postOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     postOrderTraversal(rootNode.leftChild)
#     postOrderTraversal(rootNode.rightChild)
#     print(rootNode.data)


# # postOrderTraversal(newBT)


# ######## level Order Traversal method
# def levelOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     else:
#         customQueue = queue.Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             print(root.value.data)
#             if root.value.leftChild is not None:
#                 customQueue.enqueue(root.value.leftChild)

#             if root.value.rightChild is not None:
#                 customQueue.enqueue(root.value.rightChild)


# # levelOrderTraversal(newBT)


# ####  Search Method in Trees
# def searchBT(rootNode, nodeValue):
#     if not rootNode:
#         return "the bt doesn't exist"
#     else:
#         customQueue = queue.Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             if root.value.data == nodeValue:
#                 return "Sucess"
#             if root.value.leftChild is not None:
#                 customQueue.enqueue(root.value.leftChild)

#             if root.value.rightChild is not None:
#                 customQueue.enqueue(root.value.rightChild)
#         return "Not Found"


# # print(searchBT(newBT, "tea"))


# def insertion(rootNode, newNode):
#     if not rootNode:
#         rootNode = newNode
#     else:
#         customQueue = queue.Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             if root.value.leftChild is not None:
#                 customQueue.enqueue(root.value.leftChild)
#             else:
#                 root.value.leftChild = newNode
#                 return "successfully inserted"
#             if root.value.rightChild is not None:
#                 customQueue.enqueue(root.value.rightChild)
#             else:
#                 root.value.rightChild = newNode
#                 return "Successfully Inserted"


# # newNode = TreeNode("Coka-Cola")
# # print(insertion(newBT, newNode))
# # levelOrderTraversal(newBT)


# ######## delete


# def getDeepestNode(rootNode):
#     if not rootNode:
#         return
#     else:
#         customQueue = queue.Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             if root.value.leftChild is not None:
#                 customQueue.enqueue(root.value.leftChild)

#             if root.value.rightChild is not None:
#                 customQueue.enqueue(root.value.rightChild)
#         deepestNode = root.value
#         return deepestNode


# # deepestNode = getDeepestNode(newBT)
# # print(deepestNode.data)


# def deleteDeepestNode(rootNode, dNode):
#     if not rootNode:
#         return
#     else:
#         customQueue = queue.Queue()
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


# # newNode = getDeepestNode(newBT)
# # deleteDeepestNode(newBT,newNode)
# # levelOrderTraversal(newBT)


# def deleteNodeBT(rootNode, node):
#     if not rootNode:
#         return
#     else:
#         customQueue = queue.Queue()
#         customQueue.enqueue(rootNode)
#         while not (customQueue.isEmpty()):
#             root = customQueue.dequeue()
#             if root.value.data == node:
#                 dNode = getDeepestNode(rootNode)
#                 root.value.data = dNode.data
#                 deleteDeepestNode(rootNode, dNode)
#                 return "the node has been successfully deleted"
#             if root.value.leftChild is not None:
#                 customQueue.enqueue(root.value.leftChild)

#             if root.value.rightChild is not None:
#                 customQueue.enqueue(root.value.rightChild)
#         return "failed to delete"


# # deleteNodeBT(newBT,'Drinks')
# # levelOrderTraversal(newBT)


# #############  delete Entire Binary Tree  #############
# def deleteBT(rootNode):
#     rootNode.data = None
#     rootNode.leftChild = None
#     rootNode.rightChild = None
#     return "bt has been successfully deleted"


# deleteBT(newBT)
# levelOrderTraversal(newBT)


#######################################################  practice Binary Tree using linked list ######################################


class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


newBT = BinaryTree("Drinks")
rightChild = BinaryTree("Hot")
leftChild = BinaryTree("Cold")
tea = BinaryTree("tea")
coffee = BinaryTree("coffee")

leftChild.leftChild = tea
leftChild.rightChild = coffee
newBT.rightChild = rightChild
newBT.leftChild = leftChild

def preOrderTarversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTarversal(rootNode.leftChild)
    preOrderTarversal(rootNode.rightChild)

# preOrderTarversal(newBT)

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






































###########################################    Creating Binary Tree using Python List ###########################################
# class BinaryTree:
#     def __init__(self, size):
#         self.customList = size * [None]
#         self.lastUsedIndex = 0
#         self.maxSize = size

#     def insertNode(self, value):
#         if self.lastUsedIndex + 1 == self.maxSize:
#             return "The Binary Tree is full"
#         self.customList[self.lastUsedIndex + 1] = value
#         self.lastUsedIndex += 1
#         return "The value has been successfully inserted"

#     def searchNode(self, nodeValue):
#         for i in range(len(self.customList)):
#             if self.customList[i] == nodeValue:
#                 return "success"
#         return "not found"

#     def preOrderTraversal(self, index):
#         if index > self.lastUsedIndex:
#             return
#         print(self.customList[index])
#         self.preOrderTraversal(index * 2)
#         self.preOrderTraversal(index * 2 + 1)

#     def inOrderTraversal(self, index):
#         if index > self.lastUsedIndex:
#             return
#         self.inOrderTraversal(index * 2)
#         print(self.customList[index])
#         self.inOrderTraversal(index * 2 + 1)

#     def postOrderTraversal(self, index):
#         if index > self.lastUsedIndex:
#             return
#         self.postOrderTraversal(index * 2)
#         self.postOrderTraversal(index * 2 + 1)
#         print(self.customList[index])

#     def levelOrdertravesal(self, index):
#         for i in range(index, self.lastUsedIndex + 1):
#             print(self.customList[i])

#     def deleteNode(self, value):
#         if self.lastUsedIndex == 0:
#             return "there is not any element to delete"
#         for i in range(1, self.lastUsedIndex + 1):
#             if self.customList[i] == value:
#                 self.customList[i] = self.customList[self.lastUsedIndex]
#                 self.customList[self.lastUsedIndex] = None
#                 self.lastUsedIndex -= 1
#                 return "the node has been successfully deleted"

#     def deleteBT(self):
#         self.customList = None
#         return "the node has been successfully deleted"


# newBT = BinaryTree(8)
# newBT.insertNode("Drinks")
# newBT.insertNode("Hot")
# newBT.insertNode("Cold")
# newBT.insertNode("tea")
# newBT.insertNode("coffee")
# # newBT.preOrderTraversal(1)
# # newBT.inOrderTraversal(1)
# # # newBT.postOrderTraversal(1)
# # newBT.deleteNode('Hot')
# # newBT.levelOrdertravesal(1)
# # newBT.deleteBT()
# # newBT.levelOrdertravesal(1)
