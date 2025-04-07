# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = [True]
        
        def checkHeight(root):
            if not root: 
                return 0
            # Recursively calculate the height of the left and right subtrees
            leftHeight = checkHeight(root.left)
            rightHeight = checkHeight(root.right)
            
            if abs(leftHeight- rightHeight)>1:
                balance[0] =  False
                return 0
            
            return  1 + max(leftHeight , rightHeight)

        checkHeight(root)
        return(balance[0])



                
        
         
         
         
        
         

    




        

        