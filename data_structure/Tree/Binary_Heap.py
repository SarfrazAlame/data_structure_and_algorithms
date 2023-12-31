# class Heap:
#     def __init__(self, size):
#         self.customList = (size + 1) * [None]
#         self.heapSize = 0
#         self.maxSize = size + 1


# def peekOfHeap(rootNode):
#     if not rootNode:
#         return
#     else:
#         return rootNode.customList[1]


# def sizeOfHeap(rootNode):
#     if not rootNode:
#         return
#     else:
#         return rootNode.heapSize


# def levelOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     else:
#         for i in range(1, rootNode.heapSize + 1):
#             print(rootNode.customList[i])


# def heapifyTreeInsert(rootNode, index, heapType):
#     parentIndex = int(index / 2)
#     if index <= 1:
#         return
#     if heapType == "Min":
#         if rootNode.customList[index] < rootNode.customList[parentIndex]:
#             temp = rootNode.customList[index]
#             rootNode.customList[index] = rootNode.customList[parentIndex]
#             rootNode.customList[parentIndex] = temp
#         heapifyTreeInsert(rootNode, parentIndex, heapType)
#     elif heapType == "Max":
#         if rootNode.customList[index] > rootNode.customList[parentIndex]:
#             temp = rootNode.customList[index]
#             rootNode.customList[index] = rootNode.customList[parentIndex]
#             rootNode.customList[parentIndex] = temp
#         heapifyTreeInsert(rootNode, parentIndex, heapType)


# def insertNode(rootNode, ndoeValue, headType):
#     if rootNode.heapSize + 1 == rootNode.maxSize:
#         return "The Binary Heap is full"
#     rootNode.customList[rootNode.heapSize + 1] = ndoeValue
#     rootNode.heapSize += 1
#     heapifyTreeInsert(rootNode, rootNode.heapSize, headType)
#     return "The value has been successfully inserted"


# def heapifyTreeExtract(rootNode, index, heapType):
#     leftIndex = index * 2
#     rightIndex = index * 2 + 1
#     swapChild = 0

#     if rootNode.heapSize < leftIndex:
#         return
#     elif rootNode.heapSize == leftIndex:
#         if heapType == "Min":
#             if rootNode.customList[index] > rootNode.customList[leftIndex]:
#                 temp = rootNode.customList[index]
#                 rootNode.customList[index] = rootNode.customList[leftIndex]
#                 rootNode.customList[leftIndex] = temp
#                 return
#         else:
#             if rootNode.customList[index] < rootNode.customList[leftIndex]:
#                 temp = rootNode.customList[index]
#                 rootNode.customList[index] = rootNode.customList[leftIndex]
#                 rootNode.customList[leftIndex] = temp
#                 return
#     else:
#         if heapType == "Min":
#             if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
#                 swapChild = leftIndex
#             else:
#                 swapChild = rightIndex
#             if rootNode.customList[index] > rootNode.customList[swapChild]:
#                 temp = rootNode.customList[index]
#                 rootNode.customList[index] = rootNode.customList[swapChild]
#                 rootNode.customList[swapChild] = temp
#         else:
#             if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
#                 swapChild = leftIndex
#             else:
#                 swapChild = leftIndex
#             if rootNode.customList[index] < rootNode.customList[swapChild]:
#                 temp = rootNode.customList[index]
#                 rootNode.customList[index] = rootNode.customList[swapChild]
#                 rootNode.customList[swapChild] = temp
#     heapifyTreeExtract(rootNode, swapChild, heapType)


# def extraxtNode(rootNode, heapType):
#     if rootNode.heapSize == 0:
#         return
#     else:
#         extraxtedNode = rootNode.customList[1]
#         rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
#         rootNode.customList[rootNode.heapSize] = None
#         rootNode.heapSize -= 1
#         heapifyTreeExtract(rootNode, 1, heapType)
#         return extraxtedNode


# def deleteEntireBP(rootNode):
#     rootNode.customList = None


# newHeap = Heap(5)
# insertNode(newHeap, 4, "Max")
# insertNode(newHeap, 5, "Max")
# insertNode(newHeap, 2, "Max")
# insertNode(newHeap, 1, "Max")
# print(newHeap.customList)
# extraxtNode(newHeap,'Max')
# deleteEntireBP(newHeap)
# levelOrderTraversal(newHeap)


class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1


def peekNode(rootNode):
    if not rootNode:
        return
    return rootNode.customList[1]


def sizeOfHeap(rootNode):
    if not rootNode:
        return 0
    return rootNode.heapSize


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    for i in range(1, rootNode.heapSize + 1):
        print(rootNode.customList[i])


def heapifyTreeInsert(rootNode, index, heapType):
    parantIndex = int(index / 2)
    if index <= 1:
        return
    if heapType == "Min":
        if rootNode.customList[index] < rootNode.customList[parantIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parantIndex]
            rootNode.customList[parantIndex] = temp
            return
        heapifyTreeInsert(rootNode, parantIndex, heapType)
    else:
        if rootNode.customList[index] > rootNode.customList[parantIndex]:
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parantIndex]
            rootNode.customList[parantIndex] = temp
            return
        heapifyTreeInsert(rootNode, parantIndex, heapType)


def insertNode(rootNode, nodeValue, heapType):
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is full"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "node has been successsfully inserted"


def heapifyTreeExtract(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0

    if rootNode.heapSize < leftIndex:
        return 
    elif rootNode.heapSize == leftIndex:
        if heapType == 'Min':
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
                return
        else:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
                return
    else:
        if heapType == 'Min':
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        
        else:
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = rightIndex
            else:
                swapChild = leftIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyTreeExtract(rootNode, swapChild, heapType)


def ExtractNode(rootNode,heapType):
    if not rootNode:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeExtract(rootNode, 1, heapType)
        return extractedNode
            
def deleteEntireBP(rootNode):
    rootNode.customList = None


newHeap = Heap(8)
insertNode(newHeap, 12, "Min")
insertNode(newHeap, 17, "Min")
insertNode(newHeap, 8, "Min")
insertNode(newHeap, 93, "Min")
insertNode(newHeap, 13, "Min")
insertNode(newHeap, 53, "Min")
insertNode(newHeap, 5, "Min")
insertNode(newHeap, 25, "Min")
# ExtractNode(newHeap,"Min")
# levelOrderTraversal(newHeap)
deleteEntireBP(newHeap)
