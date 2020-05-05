class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def traverse_to_next(self, entry):
        if entry.next != None:
            return self.traverse_to_next(entry.next)
        else:
            return entry


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """
    def __init__(self, length):
        self.storage = [None] * length
        self.length = length

    def fnv1(self, key, seed=0):
        """
        FNV-1 64-bit hash function
        """
        # Constants
        fnv_prime = 1099511628211
        offset_basis = 14695981039346656037

        # FNV1 hashing function
        hash = offset_basis + seed
        for char in key:
            hash = hash * fnv_prime
            hash = hash ^ ord(char)
        return hash

    def djb2(self, key):
        """
        DJB2 32-bit hash function
        """
        # Constant (a high prime number)
        hash = 5381

        # DJB2 hashing
        for char in key:
            hash = (hash * 33) + ord(char)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.length

    def put(self, key, value):
        #Store the value with the given key
        index = self.hash_index(key)
        print('index', index)
        print("boo", self.storage)
        value_at_index = self.storage[index]

        if value_at_index:
            print('value at index in put', value_at_index.value,
                  value_at_index.next)
            # Hash collisions should be handled with Linked List Chaining
            if value_at_index.next == None:
                value_at_index.next = HashTableEntry(key, value)
                #print('TableEntry if value_index.next is none', self.storage)
            else:
                last_entry = value_at_index.traverse_to_next(value_at_index)
                last_entry.next = HashTableEntry(key, value)
                #print(
                # "having to traverse the linked list, value at last entry",
                # self.storage)
        else:
            new_entry = HashTableEntry(key, value)
            self.storage[index] = new_entry
            print("affer inster", self.storage)
            #print('there was no value at index, printing new entry',

    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        """
        index = hash_index(key)
        self.storage[index] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.
        """
        index = self.hash_index(key)
        return self.storage[index].value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """


if __name__ == "__main__":
    test_list = HashTableEntry("foo", 1)
    test_list.next = HashTableEntry("bar", 2)
    test_list.next.next = HashTableEntry("baz", 3)
    test_list.next.next.next = HashTableEntry("blam", 4)

    print(test_list.traverse_to_next(test_list).key)

    # ht = HashTable(2)

    # ht.put("line_1", "Tiny hash table")
    # ht.put("line_2", "Filled to capacity")
    # ht.put("line_3", "Linked list saves the day!")

    # # Test storing beyond capacity
    # print("Test storing beyond capacity")
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    # # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    # print("")
