Chalenger deque: Make a software that can identify palindromes words
print('siple deques')

class SimpleDeque:
    def __init__(self, manual=False, head=None):
        if manual:
            self.head = input('Writh the first element:')            
        else:
            self.head = head
            self.tail = tail