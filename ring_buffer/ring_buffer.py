class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):

        if len(self.storage) == self.capacity:
            self.storage[self.current] = item
        else:
            self.storage.append(item)
        self.current = (self.current + 1) % self.capacity

    def get(self):
        storage_arr = [item for item in self.storage if item != None]

        return storage_arr
