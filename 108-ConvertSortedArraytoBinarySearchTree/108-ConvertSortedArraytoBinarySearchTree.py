# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def tree(lst):
            if not lst:
                return None
            mid = len(lst) // 2
            head = TreeNode(val=lst[mid])
            head.left = tree(lst[:mid])
            head.right = tree(lst[mid+1:])
            return head
        return tree(nums)