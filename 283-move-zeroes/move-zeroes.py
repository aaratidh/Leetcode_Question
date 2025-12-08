class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write_idx = 0 
        for i , val in enumerate(nums):
            if nums[i] != 0 :
                nums[write_idx] = nums[i]
                write_idx = write_idx + 1
        for i in range(write_idx , len(nums)):
            nums[i] = 0 




# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         l= 0 
#         r = len(nums) - 1
#         while l < r:
#             if nums[r] == 0:
#                 r = r-1
#             elif nums[l] != 0: 
#                 l = l+1
#             else:
#                 nums[l], nums[r] = nums[r] , nums[l]
#                 l = l+1 
#                 r = r - 1

#         def mergesort(arry):
#             if len(arry)<=1:
#                 return arry

#             mid = len(arry)//2 
#             left_arry = mergesort( arry[:mid])
#             right_arry = mergesort( arry[mid:])
#             #merge 
#             i = 0 
#             j = 0 
#             k = 0 
#             while  i < len(left_arry) and j < len(right_arry): 
#                 if left_arry[i] <= right_arry[j]: 
#                     arry[k] = left_arry[i]
#                     i = i + 1
#                 else: 
#                     arry[k] = right_arry[j]
#                     j = j+ 1 
#                 k = k + 1 
#             while i < len(left_arry): 
#                 arry[k] = left_arry[i]
#                 i = i + 1
#                 k = k+ 1
#             while j < len(right_arry): 
#                 arry[k] = right_arry[j]
#                 k = k + 1
#                 j = j + 1   
#             return arry
#         nums[:] = mergesort(nums[:r+1]) + nums[r+1:]
#         return nums


            











            
        




        
                

                







            
                


    
        