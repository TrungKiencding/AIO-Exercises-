class Queue():
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

    def dequeue(self):
        if not self.is_empty():
            return self.__lst.pop(0)
        
    def enqueue(self, value):
        if not self.is_full():
            return self.__lst.append(value)
    
    def front(self):
        if not self.is_empty():
            return self.__lst[0]
    

queue1 = Queue(capacity=5)

queue1.enqueue(1)
queue1.enqueue(2)

print(queue1.is_full())

print(queue1.front())

print(queue1.dequeue())

print(queue1.front())

print(queue1.dequeue())

print(queue1.is_empty())