class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000  # Choose an arbitrary size for the array
        self.buckets = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        index = self._hash(key)
        if not self.buckets[index]:
            self.buckets[index] = ListNode(key, value)
        else:
            current = self.buckets[index]
            while current:
                if current.key == key:
                    current.val = value
                    return
                if not current.next:
                    break
                current = current.next
            current.next = ListNode(key, value)

    def get(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.val
            current = current.next
        return -1

    def remove(self, key):
        index = self._hash(key)
        current = self.buckets[index]
        if not current:
            return
        if current.key == key:
            self.buckets[index] = current.next
        else:
            prev = current
            current = current.next
            while current:
                if current.key == key:
                    prev.next = current.next
                    return
                prev = current
                current = current.next