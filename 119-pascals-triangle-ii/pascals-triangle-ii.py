class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        array :list[list[int]] = []
        for i in range(rowIndex + 1):
            array.append([0]* (i+1))
            for j in range(i+1):
                if j == 0 or j == i: 
                    array[i][j] = 1
                else: 
                    array[i][j] = array[i-1][j-1]+ array[i-1][j]
        return array[rowIndex]
            
