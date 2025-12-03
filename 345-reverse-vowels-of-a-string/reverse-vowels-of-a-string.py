class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s_list = list(s)

        left, right = 0, len(s_list) - 1

        while left < right:
            # move left pointer until vowel
            while left < right and s_list[left] not in vowels:
                left += 1
            
            # move right pointer until vowel
            while left < right and s_list[right] not in vowels:
                right -= 1
            
            # swap vowels
            s_list[left], s_list[right] = s_list[right], s_list[left]
            
            left += 1
            right -= 1
        
        return "".join(s_list)
            

               
        
        
        
        
        
        
        
        
        
        
    #Solution using Stack    
        # for letter in list1: 
        #     if letter in alphabet:
        #         stack.append(letter)
        # for i, letter in enumerate(list1):
        #     if letter in alphabet:
        #         list1[i]  = stack.pop()
        # return "".join(list1)


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

            


             










        

        