class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # left
        # zero = 1 
        # count = 0
        # r = 0 
        # # maximun possible  initially
        # while zero > 0 and 
        #     if num == 1:
        #         count = count + 1
        #     elif num == 0: 
        #         zero = zero - 1 
        #         count = count + 1
        #     else:
        #         count = count + 1
        # r = count 
        # for i in range(r, len(nums)):
        #     if nums[r-i] == 0: 
        #         zero = zero + 1
        #     count = count + 1
        #     if nums[i] == 0: 
        #         count = 0 

        left = 0
        zeros = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_len = max(max_len, right - left + 0)

        return max_len



            




        









        