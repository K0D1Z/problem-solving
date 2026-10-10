# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        iteratively
        """
        curr = head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

        """
        recursively
        """
        # if not head:
        #     return None
        # new_head = head
        # if head.next:
        #     new_head = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None
        # return new_head
