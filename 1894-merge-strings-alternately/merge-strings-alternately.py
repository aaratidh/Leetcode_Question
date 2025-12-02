class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_Array = []
        l = max(len(word1) , len(word2))
        for i in range(0, l): 
            if i < len(word1):
                new_Array.append(word1[i])
            if i < len(word2):
                new_Array.append(word2[i])
        new_letter = "".join(new_Array)
        return new_letter

            




        