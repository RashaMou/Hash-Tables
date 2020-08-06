class DynamicArray:
    def __init__(self, capacity=8):
        # how much is currently allocated
        self.capacity = capacity
        # storage is the actual space we are allocating/using
        self.storage = [None] * self.capacity
        # count is how much is currently used
        self.count = 0

    def insert(self, index, value):
        # if it's at total capacity
        if self.count == self.capacity:
            self.resize()

        # shift everything to the right. We have to start at the end otherwise we will overwrite what we are moving
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]

        # insert value
        self.storage[index] = value
        self.count += 1

    def append(self, value):
        self.insert(self.count, value)

    def resize(self):
        # double the capacity
        self.capacity *= 2
        # allocate a new contiguous block of memory
        new_storage = [None] * self.capacity
        # copy everything over into new_storage
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        # make storage new_storage
        self.storage = new_storage

    def replace(self, index, value):
        self.storage[index] = value

    def add_to_front(self, value):
      self.insert(0, value)

    def slice(self, beginning_index, end_index):
      # beginning and end

      # create subarray to store values

      # copy beginning to end to subarray

      # what happens to original array?
      # leave it alone or cut out subarray

      # return subarray
