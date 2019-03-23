import array

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = 0
        self.tail = 0
        self.size = 0
        self.data = array.array("i", range(capacity))
    def empty(self):
        if self.size == 0:
            return True
        return False
    def full(self):
        if self.size == self.capacity:
            return True
        return False
    def enqueue(self, x):
        if self.size == self.capacity:
            return False
        self.data[self.tail] = x
        self.tail += 1
        self.size += 1
        return True
    def dequeue(self):
        if self.size == 0:
            return None
        value = self.data[self.head]
        self.head += 1
        self.size -= 1
        return value
    def checkRep():
        assert self.size >= 0
        assert self.tail >= 0
if __name__ == "__main__":
    pass == "__main__":
    q = Queue(1)
    if not q.empty():
        print("Check empty")
    if not q.enqueue(10):
        print("Check enqueue")
    if not q.full():
        print("Check full")
    if q.dequeue() != 10:
        print("Check dq")