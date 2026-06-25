class Node:
    def __init__(self, key, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # internal variables
        self.size = 0
        self.lru = dict()
        # doubly linked list buffer
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.lru:
            return -1
        item = self.lru[key]
        # quick return if already at the end of the lru
        if item.next == self.tail:
            # print(f"(get {key} early) lru: {self.head.next.key}, mru: {self.tail.prev.key}")
            return item.val
        
        # modify node in lru
        item.prev.next = item.next
        item.next.prev = item.prev
        item.prev = self.tail.prev
        item.next = self.tail
        self.tail.prev.next = item
        # modify tail
        self.tail.prev = item
        # print(f"(get {key}) lru: {self.head.next.key}, mru: {self.tail.prev.key}")
        return item.val

    def put(self, key: int, value: int) -> None:
        # put in lru
        node = None
        if key in self.lru:
            # update node
            node = self.lru[key]
            node.val = value
            # modify node placement
            if node.next != self.tail:
                # modify surrounding nodes
                node.prev.next = node.next
                node.next.prev = node.prev
                # modify current node
                node.prev = self.tail.prev
                node.next = self.tail
            
        else:
            # create new node
            node = Node(key, value, self.tail.prev, self.tail)
            self.lru[key] = node
            self.size += 1
        
        # update tail and tails prev
        self.tail.prev.next = node
        self.tail.prev = node

        # capacity check
        # print(f"(put ({key, value})); lru: {self.head.next.key}, mru: {self.tail.prev.key}")
        if self.size > self.capacity:
            toDel = self.head.next
            toDel.prev.next = toDel.next
            toDel.next.prev = toDel.prev
            del self.lru[toDel.key]
            del toDel
            self.size -= 1
        


