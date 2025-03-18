class Solution(object):
    def twoSum(self, nums, target):
        for  i , num in enumerate(nums):
            diffs = target - num
            if (diffs in nums) and ( i!= nums.index(diffs)):
                return i, nums.index(diffs)
                
         


