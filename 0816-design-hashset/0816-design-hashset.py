class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

LIMIT = 5_000

class MyHashSet:

    def __init__(self):
        self.arr = [Node() for _ in range(LIMIT)]
        

    def add(self, key: int) -> None:
        node = self.arr[key % LIMIT]
        while node.next:
            if node.next.val == key:
                return
            node = node.next
        node.next = Node(key)

    def remove(self, key: int) -> None:
        node = self.arr[key % LIMIT]
        while node.next:
            if node.next.val == key:
                node.next = node.next.next
                return
            node = node.next
        
    def contains(self, key: int) -> bool:
        node = self.arr[key % LIMIT]
        while node.next:
            if node.next.val == key:
                return True
            node = node.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)