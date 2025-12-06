class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0   # pointer to write compressed chars
        read = 0    # pointer to read input array
        n = len(chars)
        while read < n:
            char = chars[read]
            count = 0
            # count how many times char repeats
            while read < n and chars[read] == char:
                read += 1
                count += 1
            # write the character
            chars[write] = char
            write += 1
            # write the count if > 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

        return write

 




        