# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = {0: 1}  # base case
        self.count = 0

        def dfs(node, currSum):
            if not node:
                return

            currSum += node.val

            # check how many paths end here with sum = targetSum
            self.count += prefix.get(currSum - targetSum, 0)

            # add current sum to map
            prefix[currSum] = prefix.get(currSum, 0) + 1

            # recurse
            dfs(node.left, currSum)
            dfs(node.right, currSum)

            # backtrack
            prefix[currSum] -= 1

        dfs(root, 0)
        return self.count
        
             