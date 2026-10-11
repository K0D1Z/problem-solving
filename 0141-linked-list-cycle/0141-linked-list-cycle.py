# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''FIRST ATTEMPT'''
        # if not head or not head.next:
        #     return False

        # slow = head
        # fast = head

        # while slow and fast:
        #     slow = slow.next
        #     fast = fast.next
        #     if fast:
        #         fast = fast.next
        #     if slow == fast:
        #         return True
        # return False

        '''OPTIMAL'''
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
