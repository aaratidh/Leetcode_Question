class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurance = {}
        checklist = set()
        for num  in arr:
            if num not in occurance:
                occurance[num] = 1 
            else: 
                occurance[num] = occurance[num] + 1 
        print(occurance)
        for value in occurance.values(): 
            if value in checklist: 
                return False 
            else: 
                checklist.add(value)

        return  True 


        