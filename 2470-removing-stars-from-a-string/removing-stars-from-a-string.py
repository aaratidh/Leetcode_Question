class Solution:
    def removeStars(self, s: str) -> str:
        stack  = []
        for char in s: 
            if char is not '*':
                stack.append(char)
            else: 
                stack.pop()
        print("".join(stack))
        return "".join(stack)
            


        