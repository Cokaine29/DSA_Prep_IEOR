class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        temp = goal + goal 

        i = 0 
        j = len(goal) 

        while j <= 2 * len(goal) :
            if temp[i:j] == s :
                return True
            else :
                i += 1 
                j += 1
        return False
 