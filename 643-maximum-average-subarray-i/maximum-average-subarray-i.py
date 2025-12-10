class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        j = k
        maxsum = float('-inf')
        sum1 = sum(nums[i:j])
        maxsum = maxsum = max(sum1 , maxsum)
        while j <= len(nums)-1:
            sum1 = sum1 + nums[j] - nums[i]
            maxsum = max(sum1 , maxsum)
            i = i + 1 
            j = j + 1
        return maxsum/k





        
            




        


       

    





  


    
        

        








        




        


        
        

        

        