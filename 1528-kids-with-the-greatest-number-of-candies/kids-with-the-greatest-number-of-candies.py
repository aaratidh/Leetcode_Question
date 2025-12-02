class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_no_of_Candies = max(candies)
        return [(curr + extraCandies >= max_no_of_Candies) for curr in candies]
       





        
        