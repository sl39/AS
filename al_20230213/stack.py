# 스택 클래스 만들기
class Stack:
    def __init__(self,size):
        self.size = size
        self.items = [None] * size
        self.top = -1


    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False


    def push(self, item):
        if self.is_full():
            print('스택이 가득 차서 추가 불가')
        else:
            self.top += 1
            self.items[self.top] = item


    def peek(self):
        if self.is_empty():
            raise Exception('스택이 비었다.')
        else:
            return self.items[self.top]


    def is_full(self):
        if self.top + 1 == self.size:
            return True
        else:
            return False

    def pop(self):
        # 비어있지 않으면
        if self.is_empty():
            pass
        else:
            value = self.items[self.top]
            self.top -= 1
            return value




s1 = Stack(5)
print(s1.items)
print(s1.top)
print(s1.is_empty())

s1.push('A')
print(s1.items)
print(s1.top)
print(s1.peek())
s1.push('B')
s1.push('C')
s1.push('D')
s1.push('E')
# s2 = Stack(5)
# print(s2.peek())
print(s1.items)
print(s1.top)
print(s1.peek())
print(s1.pop())
s1.push("G")
print(s1.top)
print(s1.peek())
