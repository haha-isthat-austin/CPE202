class Queue():
    # circular buffer
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [None] * self.capacity
        self.head = 0
        self.tail = 0
        self.num_items = 0

    def is_empty(self):
        return self.num_items == 0

    def is_full(self):
        return self.num_items == self.capacity

    # put at end of list
    def enqueue(self, item):

        if self.is_full():
            raise IndexError()
        
        self.items[self.tail] = item
        self.num_items += 1

        self.tail += 1

        if self.tail >= self.capacity:
            self.tail = 0

    # grab from beginning of list
    def dequeue(self):
        if self.is_empty():
            raise IndexError()

        item = self.items[self.head]
        self.num_items -= 1
        self.head += 1

        if self.head >= self.capacity:
            self.head = 0

        return item

    def size(self):
        return self.num_items