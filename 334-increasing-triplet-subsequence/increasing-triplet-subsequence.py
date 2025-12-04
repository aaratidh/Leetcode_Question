class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        numi = float('inf')
        numj = float('inf')
        for num in nums:
            if num <= numi: 
                numi = num 
            elif num <= numj:
                numj = num
            else: 
                return True
        return False
                
[5,4,3,2,1]
          

[1,2,3,4,5]
        