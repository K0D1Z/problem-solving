class Node:
    def __init__(self, key = -1, value = -1, next = None):
        self.key = key
        self.value = value
        self.next = next

LIMIT = 5_000

class MyHashMap:

    def __init__(self):
        self.arr = [Node() for _ in range(LIMIT)]

    def hash(self, key: int):
        return key % LIMIT

    def put(self, key: int, value: int) -> None:
        node = self.arr[self.hash(key)]
        while node.next:
            if node.next.key == key:
                node.next.value = value
                return
            node = node.next
        node.next = Node(key, value)

    def get(self, key: int) -> int:
        node = self.arr[self.hash(key)]
        while node.next:
            if node.next.key == key:
                return node.next.value
            node = node.next
        return -1
        

    def remove(self, key: int) -> None:
        node = self.arr[self.hash(key)]
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next


# class MyHashSet:

#     def __init__(self):
#         self.arr = [Node() for _ in range(LIMIT)]
        

#     def add(self, key: int) -> None:
#         node = self.arr[key % LIMIT]
#         while node.next:
#             if node.next.val == key:
#                 return
#             node = node.next
#         node.next = Node(key)

#     def remove(self, key: int) -> None:
#         node = self.arr[key % LIMIT]
#         while node.next:
#             if node.next.val == key:
#                 node.next = node.next.next
#                 return
#             node = node.next
        
#     def contains(self, key: int) -> bool:
#         node = self.arr[key % LIMIT]
#         while node.next:
#             if node.next.val == key:
#                 return True
#             node = node.next
#         return False

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)