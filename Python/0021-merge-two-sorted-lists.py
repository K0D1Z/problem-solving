# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        head = node
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                node.next = list1
                node = node.next
                list1 = list1.next
            else:
                node.next = list2
                node = node.next
                list2 = list2.next
        while list1 is not None:
            node.next = list1
            node = node.next
            list1 = list1.next
        while list2 is not None:
            node.next = list2
            node = node.next
            list2 = list2.next
        return head.next

