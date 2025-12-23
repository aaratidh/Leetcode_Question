class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum1 = 0 
        leftsum = 0
        for num in nums: 
            sum1 = sum1 + num
        
        for i in range(len(nums)):
            if i == 0: 
                if sum1 - nums[i] == 0:
                    return 0
            else:
                leftsum = leftsum + nums[i-1]
                rightsum = sum1 - leftsum - nums[i]
                if leftsum == rightsum: 
                    return i 
        return -1 







        