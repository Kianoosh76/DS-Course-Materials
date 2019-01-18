class HashTable:
    class _Cell:
        def __init__(self, key: int, value: object) -> None:
            self._key = key
            self._value = value
            self._isDeleted = False

        def get_key(self):
            return self._key

        def get_value(self):
            return self._value

        def is_deleted(self):
            return self._isDeleted

        def delete(self):
            self._isDeleted = True

    def __init__(self, size):
        self._size = size
        self._table = [None for _ in range(size)]

    def _hash(self, key, i):
        return (key + i) % self._size

    def insert(self, key, value):
        for i in range(self._size):
            cell: HashTable._Cell = self._table[self._hash(key, i)]
            if cell is None or cell.is_deleted():
                self._table[self._hash(key, i)] = HashTable._Cell(key, value)
                return True
        return False

    def delete(self, key):
        for i in range(self._size):
            cell: HashTable._Cell = self._table[self._hash(key, i)]
            if cell is None:
                break
            if cell.get_key() == key:
                cell.delete()
                break

    def get(self, key):
        for i in range(self._size):
            cell: HashTable._Cell = self._table[self._hash(key, i)]
            if cell is None:
                return None
            if not cell.is_deleted() and cell.get_key() == key:
                return cell.get_value()

