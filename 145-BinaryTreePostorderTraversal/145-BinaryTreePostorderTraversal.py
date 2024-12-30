# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        st = [root]
        while st:
            tmp = st.pop()
            res.append(tmp.val)

            if tmp.left:
                st.append(tmp.left)

            if tmp.right:
                st.append(tmp.right)
                
        res.reverse()
        return res
            
