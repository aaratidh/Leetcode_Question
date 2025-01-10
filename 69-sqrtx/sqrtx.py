class Solution:
    def mySqrt(self, x: int) -> int:
        found = 1 
        i = 0
        while(found):
            if x == ((i+1)*(i+1)):
                found = 0 
                return i+ 1
            elif x >= (i*i) and x < ((i+1)*(i+1)):
                found = 0
                return i 
            i = i + 1
        



        


        