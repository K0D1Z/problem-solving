# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''STARTING WITH JUST ORDINARY SLOW AND FAST POINTER
        OPPROACH TO DETECT LINKED LIST CYCLE'''
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                '''CYCLE DETECTED - SET SLOW POINTER TO HEAD
                AND ADVANCE EACH POINTER BY ONLY ONE NODE'''
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None