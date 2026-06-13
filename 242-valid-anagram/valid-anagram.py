class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # # Approach 1 
        if len(s) != len(t) :
            return False 
        d = {}

        for c in s :
            if c in d :
                d[c] += 1 
            else :
                d[c] = 1 
        
        for c in t :
            if c in d :
                d[c] -= 1 
            else :
                return False 
        for ele in d :
            if d[ele] != 0 :
                return False 
        return True

        ## Approach 2 


        # return True if sorted(s) == sorted(t) else False         