class Solution:
    def secondHighest(self, s: str) -> int:
        d = {"0","1","2","3","4","5","6","7","8","9"}
        m1 = -1
        m2 = -1 

        for i in s :
            if i in d :
                if int(i) > m1 :
                    m2 = m1 
                    m1 = int(i) 
                elif int(i) < m1 and int(i) > m2 :
                    m2 = int(i)               
        return m2  

        