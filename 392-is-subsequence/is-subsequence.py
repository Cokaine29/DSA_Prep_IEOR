class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0 :
            return True
        elif len(s) !=0 and len(t) == 0 :
            return False

        i = 0 
        j = 0

        while True :
            if s[i] == t[j] :
                i += 1 
                j += 1
            else :
                j += 1
            if j == len(t) or i == len(s) :
                break
        if i == len(s) :
            return True
        elif i < len(s) :
            return False
        