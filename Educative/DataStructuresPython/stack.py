class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, el):
        self.items.append(el)
    
    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items
    
    def is_empty(self):
        return self.items == []
    