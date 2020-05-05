class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def get_last_entry(self, entry):
        if entry.next != None:
            return self.get_last_entry(entry.next)
        else:
            return entry

    def find_entry(self, key):
        current = self

        while current != None:
            if current.key == key:
                return current

            current = current.next

        return None


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
        # Find the hash index
        index = self.hash_index(key)
        # print(index)
        list_at_index = self.storage[index]
        # If the index in storage has a list
        if list_at_index != None:
            # Search the list for the key
            searched_entry = list_at_index.find_entry(key)
            # If it's there, replace the value
            if searched_entry != None:
                searched_entry.key = key
                searched_entry.value = value
                # print("searched entry", searched_entry.value)
            # If it's not, append a new record to the list
            else:
                last_entry = list_at_index.get_last_entry(list_at_index)
                last_entry.next = HashTableEntry(key, value)
                # print("last entry.next", last_entry.next)
        # Else if the index has no list, start a new one at that index
        else:
            new_entry = HashTableEntry(key, value)
            self.storage[index] = new_entry
            # print("index:", index, "new_entry:", new_entry)

    def delete(self, key):
        """
        Find the hash index
        Search the list for the key
        If found, delete the node from the list, (return the node or value?)
        Else return None
        """
        index = hash_index(key)
        to_be_deleted = self.storage[index].find_entry(key)

    def get(self, key):
        """
        Find the hash index
        Search the list for the key
        If found, return the value
        Else return None
        """
        index = self.hash_index(key)

        return self.storage[index].find_entry(key).value

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """


if __name__ == "__main__":
    # test_list = HashTableEntry("one", 1)
    # test_list.next = HashTableEntry("two", 2)
    # test_list.next.next = HashTableEntry("three", 3)
    # test_list.next.next.next = HashTableEntry("four", 4)

    # print(test_list.find_entry("five"))

    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled to capacity")
    ht.put("line_3", "Now it's different")

    # Test storing beyond capacity
    print("Test storing beyond capacity")
    print(ht.get("line_1").value)
    print(ht.get("line_2").value)
    print(ht.get("line_3").value)

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
