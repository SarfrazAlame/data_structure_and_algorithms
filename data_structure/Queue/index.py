class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return " ".join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "element inserted successfully"

    def dequeue(self):
        if self.isEmpty():
            return "There is not any element to remove"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "There is not any element to remove"
        else:
            return self.items[0]

    def delete(self):
        self.items = None


customQueue = Queue()
# print(customQueue.isEmpty())
customQueue.enqueue(10)
customQueue.enqueue(20)
customQueue.enqueue(30)
customQueue.enqueue(40)
# print(customQueue)
# print(customQueue.dequeue())
print(customQueue.peek())
customQueue.delete()