# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value, storage=None):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''

        storage = storage if storage else self.storage

        index = self._hash_mod(key)
        kv = LinkedPair(key, value)

        if storage[index] is not None:
            '''
            if there is already a linked list at this index,
            traverse the list until you find the key or next is None
            '''
            current_pair = storage[index]

            while current_pair.next and current_pair.key is not key:
                current_pair = current_pair.next
            
            if current_pair.key is key:
                current_pair.value = value
            else:
                current_pair.next = kv

        else:
            storage[index] = kv

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        def find(kv, key, prev=None):
            if not kv:
                print('key not found')

            elif kv.key is key:
                kv.value = None

            else:
                find(kv.next, key, kv)

        index = self._hash_mod(key)

        return find(self.storage[index], key)


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        def find(kv,key):
            if not kv:
                return None

            if kv.key is key:
                return kv.value
            
            return find(kv.next, key)

        index = self._hash_mod(key)

        if self.storage[index] is not None:
            return find(self.storage[index], key)

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for slot in self.storage:
            if not slot:
                continue
                
            current_pair = slot

            while current_pair:
                self.insert(current_pair.key, current_pair.value, new_storage)
                current_pair = current_pair.next
        
        self.storage = new_storage

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
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