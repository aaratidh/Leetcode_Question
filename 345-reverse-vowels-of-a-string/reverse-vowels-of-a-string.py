class Solution:
    def reverseVowels(self, s: str) -> str:
        list1 = list(s)
        alphabet = ['a','e','i','o','u' ,'A', 'E','I','O','U']
        stack = []
        for letter in list1: 
            if letter in alphabet:
                stack.append(letter)
        for i, letter in enumerate(list1):
            if letter in alphabet:
                list1[i]  = stack.pop()
        return "".join(list1)



        






    #solution for O(n)
        # list1 = list(s)
        # alphabet = ['a','e','i','o','u' ,'A', 'E','I','O','U']
        # alph_in_list = []
        # #check for alphabet
        # for i, letter in enumerate(list1):
        #     if letter in alphabet:
        #         alph_in_list.append(letter)
        # #reverse_alphabet_order
        # rev = alph_in_list[::-1]
        # #replace 
        # j = 0 
        # for i , letter in enumerate(list1):
        #     if letter in alphabet:
        #         list1[i] = rev[j]
        #         j = j + 1
        # return("".join(list1))

            


             










        

        