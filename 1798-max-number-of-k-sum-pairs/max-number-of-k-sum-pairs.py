class Solution:
    def maxOperations(self, nums, k) -> int:
        nums.sort()
        ops = 0 
        i , j  = 0 , len(nums)-1
        while i < j: 
            s = nums[i] + nums[j]
            if s == k:
                ops = ops + 1
                i = i + 1
                j = j -1
            elif s >  k :
                j = j - 1
            else: 
                i = i + 1
        return ops  



    #     def maxOperations(nums, k):
    # nums.sort()
    # i, j = 0, len(nums) - 1
    # ops = 0
 
    # while i < j:
    #     s = nums[i] + nums[j]
    #     if s == k:
    #         ops += 1
    #         i += 1
    #         j -= 1
    #     elif s < k:
    #         i += 1
    #     else:  # s > k
    #         j -= 1
 
    # return ops



      



















    # def maxOperations(self, nums: List[int], k: int) -> int:
    #     total = 0                          # how many pairs we found
    #     counter = collections.Counter()    # numbers we have waiting for a match

    #     for x in nums:
    #         # complement we need to form k
    #         if k - x in counter:           # have we already seen a number = k - x?
    #             total += 1                 # yes → we can form a pair
    #             counter[k - x] -= 1        # use one copy of that complement
    #             if counter[k - x] == 0:    # if no more copies left
    #                 del counter[k - x]     # remove it from the counter
    #             continue                   # go to next number
    #         # otherwise, save this number to maybe pair later
    #         counter[x] += 1

    #     return total

  
