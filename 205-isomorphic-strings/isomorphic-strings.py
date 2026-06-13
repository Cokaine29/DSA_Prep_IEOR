class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        l1 = len(s)
        l2 = len(t) 

        if l1 != l2 :
            return False 
        
        d = {}
        rhs = set() 

        for i in range(l1) :
            if s[i] in d :
                if d[s[i]] == t[i] :
                    pass
                else :
                    return False
            else :
                if t[i] in rhs :
                    return False 
                else :
                    d[s[i]] = t[i] 
                    rhs.add(t[i])
        return True

        