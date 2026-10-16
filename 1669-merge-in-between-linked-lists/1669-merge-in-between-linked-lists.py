# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        first = None
        last = None
        counter = 0
        node = list1
        while node:
            if counter == a - 1:
                first = node
            if counter == b + 1:
                last = node
            node = node.next
            counter += 1
        
        first.next = list2

        node = list2
        while node.next:
            node = node.next
        
        node.next = last
        return list1
        # print(first)
        # print(last)
            
            
        