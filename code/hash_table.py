class Item(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def set(self, key, value):
        hash_index = self._hash(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))

    def get(self, key):
        hash_index = self._hash(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError('Key not found')

    def remove(self, key):
        hash_index = self._hash(key)
        for index, item in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return
        raise KeyError('Key not found')


h = HashTable(5)
h.set(10, 'A')
h.set(11, 'B')
h.set(12, 'C')
h.set(13, 'D')
h.set(18, 'E')

print(h.get(10))
print(h.get(11))
print(h.get(12))
print(h.get(13))
print(h.get(18))

h.remove(12)
