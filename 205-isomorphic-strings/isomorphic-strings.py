class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        ## Approach 1 

        # l1 = len(s)
        # l2 = len(t) 

        # d = {}
        # rhs = set() 

        # for i in range(l1) :
        #     if s[i] in d :
        #         if d[s[i]] == t[i] :
        #             pass
        #         else :
        #             return False
        #     else :
        #         if t[i] in rhs :
        #             return False 
        #         else :
        #             d[s[i]] = t[i] 
        #             rhs.add(t[i])
        # return True

        ## Approach 2 

        m1 = [0] * 256
        m2 = [0] * 256 

        for i in range(len(s)) :
            if m1[ord(s[i])] == m2[ord(t[i])] :
                m1[ord(s[i])] = i + 1 
                m2[ord(t[i])] = i + 1
            else :
                return False 
        return True 

        