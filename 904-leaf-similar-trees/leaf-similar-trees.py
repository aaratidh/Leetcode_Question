# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaf1 , leaf2 = [] ,[]
        stack =[]
        def dfs(root , leaf ):
            if not root: 
                return
            stack = [root]
            while stack:
                root = stack.pop()
                if root:
                    stack.append(root.left)
                    stack.append(root.right)
                    if root.left is  None and root.right is None: 
                        leaf.append(root.val)
            return leaf
        leaf1 = dfs(root1, leaf1 )
        leaf2  = dfs(root2,  leaf2)
        return leaf1 == leaf2




        









