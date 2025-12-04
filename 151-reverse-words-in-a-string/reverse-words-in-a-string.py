class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = s.split()
        l = 0 
        r = len(list1) - 1
        while l<r:
            list1[l] , list1[r] = list1[r] , list1[l]
            l = l +1 
            r  = r -1
        return (" ".join(list1))



        

        