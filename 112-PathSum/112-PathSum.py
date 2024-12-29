# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def search(head, val=0):
            if not head:
                return False
            if not head.left and not head.right:
                if targetSum == (val + head.val):
                    return True
                return False
            t = val + head.val
            return search(head.left, t) or search(head.right, t)
        return search(root)
        
        