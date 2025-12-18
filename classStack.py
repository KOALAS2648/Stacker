from Errors import *
class Stack:
    def __init__(self, MAX_SIZE):
        self.data = []
        self.MAX_SIZE = MAX_SIZE
        self.top_pointer = -1
    def push(self, inp):
        self.top_pointer +=1
        if self.top_pointer > self.MAX_SIZE:
            raise StackOverFlow("stack overflow error")
        self.data.insert(self.top_pointer, inp)
        
    def pop(self):
        if self.top_pointer == -1:
            raise StackUnderFlow("stack underflow error")
        self.data.pop(self.top_pointer)
        self.top_pointer -=1
    def peek(self):
        if not self.isEmpty():
            return self.data[self.top_pointer]
        else:
            return -1
    def isEmpty(self):
        return self.top_pointer == -1
    def isFull(self):
        return self.top_pointer == self.MAX_SIZE
    def size(self):
        return self.top_pointer
if __name__ == "__main__":
    a = Stack(10)

    for i in range(1,11):
        a.push(i)

    a.pop()
    a.pop()
    print(a.peek())
    while not a.isEmpty():
        a.pop()

    print(a.isEmpty())