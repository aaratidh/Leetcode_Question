class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        elec = list(senate)
        R , D = Deque() , Deque() 
        for i in range(len(elec)):
            if elec[i]  == "R":
                R.append(i)
            else: 
                D.append(i)
    
        while D and R: 
            dturn = D.popleft()
            rturn = R.popleft()

            if  dturn > rturn: 
                R.append(rturn + len(elec))
            else: 
                D.append(dturn + len(elec)) 
        
        return "Radiant" if R else "Dire"

              



        


        