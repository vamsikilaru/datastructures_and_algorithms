
class Stack:

    def __init__(self) -> None:
        self.stack  = []
        self.stack_size = 0
    def is_empty(self):
        return self.stack_size == 0
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None
    def size(self):
        return self.stack_size
    def pop(self):
        if self.is_empty():
            return None
        self.stack_size -=1
        return self.stack.pop()
    def push(self,value):
        self.stack_size +=1
        self.stack.append(value)