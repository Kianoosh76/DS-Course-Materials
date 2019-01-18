from task import LRUCache
from test_helper import failed
import random


class LRUCacheSol:
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
        self._hashTable = {}

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
        self._hashTable[key] = self._rear

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
        self._hashTable.pop(key)
        self._size -= 1

    def pop(self):
        key = None
        if self._front is not None:
            key = self._front.key
            self._front = self._front.prev
            self._front.next = None
            self._hashTable.pop(key, None)
        self._size -= 1
        return key

    def get(self, key):
        if key not in self._hashTable:
            return None
        node = self._hashTable[key]
        self.delete(key)
        self.push(key, node.value)
        return node.value


if __name__ == '__main__':
    cache = LRUCache(100)
    sol = LRUCacheSol(100)
    keys = random.sample(range(0, 10 ** 10), 100000)
    for key in keys:
        if random.randint(0, 1) == 0:
            cache.add(key, key / 3)
            sol.add(key, key / 3)
        else:
            if cache.get(key) != sol.get(key):
                failed()
