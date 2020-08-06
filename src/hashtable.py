# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"<{self.key}, {self.value}>"


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        """
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        """
        return hash(key)

    def _hash_djb2(self, key):
        """
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        """
        pass

    def _hash_mod(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """
        Store the value with the given key.
        """
        # hashmod they key to find the index that we're going to store the key/value pair in.
        index = self._hash_mod(key)
        # check if something already exists at that index:
        if self.storage[index] is not None:
            # if it does exist, then turn it into starting point for linked list
            node = self.storage[index]
            # traverse linked list. Here we have three possibilities:
            # if key of next node == key, then we overwrite the value
            # if key of next node != key, then we move on
            # if key of next node == None, then we insert

            while node is not None:
                if node.key == key:
                    node.value = value
                    return
                elif node.next is not None:
                    node = node.next
                else:
                    node.next = LinkedPair(key, value)
                    return

        # if not, then insert it
        else:
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        """
        # get index from hashmod
        index = self._hash_mod(key)

        # check if a pair exists at the index:
        if self.storage[index] is not None:
            # if keys match, remove
            if self.storage[index].key == key:
                self.storage[index] = None
            # if they don't match, traverse list to see if any other node keys match it
            else:
                node = self.storage[index]
                while node.next is not None:
                    if node.next.key == key:
                        node.next = None
                    else:
                        node = node.next
        else:
            print("Key does not exist")

    def retrieve(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        """
        # get index from hashmod
        index = self._hash_mod(key)

        # check if a pair exists at that index
        if self.storage[index] is not None:
            node = self.storage[index]
            while node is not None:
                if node.key == key:
                    return node.value
                else:
                    node = node.next
        else:
            return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        """
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for item in old_storage:
            while item:
                self.insert(item.key, item.value)
                item = item.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
