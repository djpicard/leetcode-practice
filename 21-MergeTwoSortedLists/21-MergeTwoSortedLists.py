# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        def merge(l1, l2):
            out = None

            if l1 is None and l2 is None:
                return

            if l1 is None and l2 is not None:
                return l2
            
            if l1 is not None and l2 is None:
                return l1

            if l1.val <= l2.val:
                out = l1
                out.next = merge(l1.next, l2)

            if l1.val > l2.val:
                out = l2
                out.next = merge(l1, l2.next)

            return out

        return merge(list1, list2)
            