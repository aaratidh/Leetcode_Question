# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(
            self.helper(root.left, True, 1),
            self.helper(root.right, False, 1)
        )

    def helper(self, root, isLeft, depth):
        if not root:
            return depth - 1

        if isLeft:
            return max(
                self.helper(root.right, False, depth + 1),  # continue zigzag
                self.helper(root.left, True, 1)              # restart
            )
        else:
            return max(
                self.helper(root.left, True, depth + 1),     # continue zigzag
                self.helper(root.right, False, 1)             # restart
            )
        
 





        



        