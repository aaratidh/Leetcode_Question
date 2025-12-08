class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write_idx = 0  # Pointer for where the next non-zero element should be written
        
        # 1. Iterate through the array and place all non-zero elements at the beginning
        for i in range(len(nums)):
            if nums[i] != 0:
                # Place the non-zero element at the 'write' position
                nums[write_idx] = nums[i]
                write_idx += 1
                
        # 2. Fill the rest of the array (from write_idx onwards) with zeroes
        for i in range(write_idx, len(nums)):
            nums[i] = 0
            
        # No return statement is needed for in-place modification




















# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         l= 0 
#         r = len(nums) - 1
#         while l < r:
#             if nums[l] == 0 and nums[r] == 0:
#                 r = r-1
#             elif nums[l] != 0 and nums[r] == 0:
#                 r = r-1  
#                 l = l-1
#             elif nums[l] != 0 and nums[r] != 0: 
#                 l = l+1
#             else:
#                 nums[l], nums[r] = nums[r] , nums[l]
#                 l = l+1 
#                 r = r - 1

#         def mergesort(arry):
#             if len(arry)> 1:
#                 left_arry =  arry[:len(arry)//2]
#                 right_arry = arry[len(arry)//2:]
#                 mergesort(left_arry)
#                 mergesort(right_arry)
#             #merge 
#                 i = 0 
#                 j = 0 
#                 k = 0 
#                 while  i < len(left_arry) and j < len(right_arry): 
#                     if left_arry[i] > right_arry[j]: 
#                         arry[k] = right_arry[j]
#                         j = j + 1
#                     else: 
#                         arry[k] = left_arry[i]
#                         i = i+ 1 
#                     k = k + 1 
#                 while i < len(left_arry): 
#                     arry[k] = left_arry[i]
#                     i = i + 1
#                     k = k+ 1
#                 while j < len(right_arry): 
#                     arry[k] = right_arry[j]
#                     k = k + 1
#             print(arry)
#             return arry
#         nums= mergesort(nums[0:r+1]) + nums[r+1:]
#         return nums


            











            
        




        
                

                







            
                


    
        