# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, root.val)]
        count = 0
        while stack:
            node, max_so_far = stack.pop()
            if node:
                new_max = max(max_so_far, node.val)
                if node.val >= max_so_far:
                    count = count + 1
                stack.append((node.left , new_max))
                stack.append((node.right ,  new_max))
        return count



           


