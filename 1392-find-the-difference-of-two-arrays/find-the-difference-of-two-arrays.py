class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1 = set()
        num2 =set()
        for num in nums1:
            if num not in nums2:
                num1.add(num)
        for num in nums2: 
            if num not in nums1:
                num2.add(num)
        return [list(num1)] + [list(num2)]


        