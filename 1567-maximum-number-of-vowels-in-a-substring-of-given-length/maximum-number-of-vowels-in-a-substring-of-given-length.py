class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0 
        maxcount = count 
        v = {'a', 'e', 'i', 'o', 'u'}
        for i in range(k):
            if s[i] in v: 
                count = count + 1
        maxcount = max(count , maxcount) 
        for i in range(k , len(s)):
            if s[i - k] in v:
                count = count - 1
            if s[i] in v:
                count = count + 1
            maxcount = max(count , maxcount) 

        return maxcount





                

            

   

        
        