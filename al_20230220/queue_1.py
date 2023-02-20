class Queue:
    def __init__(self,n):
        self.size = n # 전체 크기
        self.items = [None] * n # 각 아이템
        self.rear = -1 # rear
        self.front = -1 # front

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return  self.rear == self.size - 1

    def Peek(self):
        return self.items[self.front]

    def enQueue(self, item):
        if self.isFull():
            print('is Full')
        else:
            self.rear += 1
            self.items[self.rear] = item

    def deQueue(self):
        if self.isEmpty():
            print('is Empty')
        else:
            self.front += 1
            item = self.items[self.front]
            self.items[self.front] = None
            return item

