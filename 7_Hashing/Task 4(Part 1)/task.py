from hash_table import HashTable


class LRUCache:
    def __init__(self, size):
        self._time_queue = Queue(size)

    def get(self, key):
        return self._time_queue.get(key)

    def add(self, key, value):
        self._time_queue.push(key, value)


class Queue:
    class Node:
        def __init__(self, prev, key, value, next):
            self.prev = prev
            self.key = key
            self.value = value
            self.next = next

    def __init__(self, size):
        self._size = 0
        self._max = size
        self._front = None
        self._rear = None
        self._hashTable = HashTable(100 * size)

    def push(self, key, value):
        if self._rear is None:
            self._rear = Queue.Node(None, key, value, None)
            self._front = self._rear
        else:
            self._rear.prev = Queue.Node(None, key, value, self._rear)
            self._rear = self._rear.prev
        self._size += 1
        if self._size > self._max:
            self.pop()
        self._hashTable.insert(key, self._rear)

    def delete(self, key):
        node = self._hashTable.get(key)
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self._rear = node.next
        if node.next is not None:
            node.next.prev = node.prev
        else:
            self._front = node.prev
        self._hashTable.delete(key)
        self._size -= 1

    def pop(self):
        key = None
        if self._front is not None:
            key = self._front.key
            self._front = self._front.prev
            self._front.next = None
            self._hashTable.delete(key)
        self._size -= 1
        return key

    def get(self, key):
        node = self._hashTable.get(key)
        if node is not None:
            self.delete(key)
            self.push(key, node.value)
            return node.value
        return None
