class node:
    def __init__(self,key =0, val =0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.right = node
        self.left = node
        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        n = node(key, value)
        self._insert(n)
        self.cache[key] = n

        if len(self.cache)>self.cap:
            lru =self.left.next
            self._remove(lru)
            del self.cache[lru.key]
    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def _insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev = prev
        prev.next = node
        node.next = nxt
        nxt.prev = node

# use doubly linked list and hashmap
# left is (least), right is most
# we use two helper functions remnove and insert
# tc: O(1), sc: O(n)
