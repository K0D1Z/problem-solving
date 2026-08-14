# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
BASE = 10


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        node = result
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            value = val1 + val2 + carry
            carry = value // BASE
            value %= BASE

            node.next = ListNode(value)
            node = node.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next
