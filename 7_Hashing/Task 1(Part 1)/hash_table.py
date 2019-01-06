class HashTable:
    class _Node:
        def __init__(self, prev, next, key, value):
            self._prev = prev
            self._next = next
            self._key = key
            self._value = value

        def prev(self):
            return self._prev

        def next(self):
            return self._next

        def key(self):
            return self._key

        def value(self):
            return self._value

        def set_prev(self, prev):
            self._prev = prev

        def set_next(self, next):
            self._next = next

    def __init__(self, size):
        self._size = size
        self._table = [None for i in range(size)]

    def _hash(self, key):
        return key % self._size

    def insert(self, key, value):
        key_hash = self._hash(key)
        if self._table[key_hash] is None:
            node = HashTable._Node(None, None, key, value)
            self._table[key_hash] = node
        else:
            node = self._table[key_hash]
            while node.next() is not None:
                node = node.next()
            new_node = HashTable._Node(node, None, key, value)
            node.set_next(new_node)

    def get(self, key):
        key_hash = self._hash(key)
        if self._table[key_hash] is None:
            return None
        else:
            node = self._table[key_hash]
            while node is not None:
                if node.key() == key:
                    return node.value()
                node = node.next()
            return None
