class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list1 = [] 
        array: List[List[int]] = []
        for i in range(numRows):
            # make the row
            array.append([0] * (i + 1))
            for j in range(i + 1):
                if j == 0 or j == i:                 # edges are 1
                    array[i][j] = 1
                else:                                 # middle = sum of two above
                    array[i][j] = array[i-1][j-1] + array[i-1][j]
        return array
                

            
    