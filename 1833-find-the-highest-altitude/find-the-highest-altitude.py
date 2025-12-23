class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        a = [0] + gain 
        diff = 0 
        print(a)
        for i in range(1 , len(gain)+1):
            a[i] = a[i-1] + gain[i-1]
        return (max(a))



            