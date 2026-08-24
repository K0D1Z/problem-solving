# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head

        # while node is not None:
        #     while node.val == node.next.val:
        #         if node.next is None:
        #             return head
        #         node.next = node.next.next
        #     node = node.next

        # return head
                
        while node is not None:
            if node.next is None:
                return head
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        