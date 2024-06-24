class Stack():
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__lst = []
    
    def is_empty(self):
        if len(self.__lst) == 0:
            return True
        else: return False
    def is_full(self):
        if len(self.__lst) == self.__capacity:
            return True
        else: return False

    def pop(self):
        if not self.is_empty():
            return self.__lst.pop()
        
    def push(self, value):
        if not self.is_full():
            return self.__lst.append(value)
    
    def top(self):
        if not self.is_empty():
            return self.__lst[-1]
    

stack1 = Stack(capacity=5)

stack1.push(1)
stack1.push(2)

print(stack1.is_full())

print(stack1.is_empty())

print(stack1.top())

print(stack1.pop())

print(stack1.top())

print(stack1.pop())

print(stack1.is_empty())