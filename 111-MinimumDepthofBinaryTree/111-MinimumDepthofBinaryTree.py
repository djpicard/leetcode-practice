# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def depth(head):
            if head is None:
                return 0
            if head.left is None and head.right is None:
                return 1
            if head.left is None:
                return 1 + depth(head.right)
            if head.right is None:
                return 1 + depth(head.left)
            return min(depth(head.left), depth(head.right)) + 1
        return depth(root)