class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        print(rf"last word is'{words[-1]} with length,{len(words[-1])}")
        return len(words[-1])
        




        