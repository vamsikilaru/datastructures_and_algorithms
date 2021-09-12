
class Queue:

    def __init__(self) -> None:
        self.queue = []
        self.queue_size = 0
    def size(self):
        return self.queue_size
    def is_empty(self):
        return self.queue_size ==0
    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]
    def rear(self):
        if self.is_empty():
            return None
        return self.queue[-1]
    def dequeue(self):
        if self.is_empty():
            return None
        self.queue_size -=1
        front = self.front
        self.queue.remove(self.front())
        return front
    def enqueue(self,value):
        self.queue_size +=1
        self.queue.append(value)