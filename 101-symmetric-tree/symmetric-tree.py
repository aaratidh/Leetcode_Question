# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = []
        queue.append(root)
        queue.append(root)

        while len(queue): #2
            left = queue[0]
            queue.pop(0)
            right = queue[0]
            queue.pop(0)

            if left.val != right.val:
                return False 
            if left.left and right.right: 
                queue.append(left.left)
                queue.append(right.right)
            elif left.left or right.right:
                return False 
            if left.right and right.left:
                queue.append(left.right)
                queue.append(right.left)
            elif left.right or right.left:
                return False
        return True
    

   

                

        





















 









    

        
              













        