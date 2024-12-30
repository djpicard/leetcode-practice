# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def compare(node):
            out = []

            if node:
                out.append(node.val)
            else:
                return []

            if node.left:
                out = out + compare(node.left)
            else:
                out.append("null")

            if node.right:
                out = out + compare(node.right)
            else:
                out.append("null")
            
            return out

        outa = compare(q)
        outb = compare(p)
        print(f"a:{outa} b:{outb}")
        return outa == outb