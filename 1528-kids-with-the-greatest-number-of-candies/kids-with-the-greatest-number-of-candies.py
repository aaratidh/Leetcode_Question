class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        bool_arry = [0] * len(candies)
        max_no_of_Candies = max(candies)
        for i  in  range(0,len(candies)):
            if candies[i] + extraCandies >=  max_no_of_Candies: 
                bool_arry[i] = True
            else:
                bool_arry[i] = False 
        return bool_arry






        
        