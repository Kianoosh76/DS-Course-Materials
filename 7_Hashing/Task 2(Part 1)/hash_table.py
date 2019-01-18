class HashTable:

    def __init__(self, size):
        self._size = size
        self._table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self._size

    def insert(self, key, value):
        key_hash = self._hash(key)
        self._table[key_hash].append((key, value))

    def get(self, key):
        key_hash = self._hash(key)
        for pair in self._table[key_hash]:
            if key == pair[0]:
                return pair[1]
        return None
