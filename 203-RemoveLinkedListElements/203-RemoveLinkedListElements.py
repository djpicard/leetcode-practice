# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # move head if head val needs to be removed
        while head and head.val == val:
            head = head.next

        # once head is setup remove all other bad vals
        tmp = head
        while tmp:
            if tmp.next and tmp.next.val == val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return head
                