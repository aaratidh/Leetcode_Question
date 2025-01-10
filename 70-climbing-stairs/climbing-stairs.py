class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2 or n == 1: 
            return n
        cur = 2
        perv = 1

        for i in range(2 , n):
            cur , perv = cur+ perv , cur
        
        return cur
        