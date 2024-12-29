# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traversal(head):
            out = []

            if not head:
                return []

            if head and head.left:
                out.extend(traversal(head.left))
            
            out.append(head.val)

            if head and head.right:
                out.extend(traversal(head.right))
            
            return out
        return traversal(root)

                