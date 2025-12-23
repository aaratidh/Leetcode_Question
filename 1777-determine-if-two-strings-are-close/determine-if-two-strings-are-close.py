class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counterword1 = Counter(word1)
        counterword2 = Counter(word2) 
        print(counterword2.values())
        print(counterword1.values())
        if sorted(list(counterword2.values())) == sorted(list(counterword1.values())) and sorted(list(counterword2.keys())) == sorted(list(counterword1.keys())):
            return True 

        return False

        