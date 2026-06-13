class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ans = ""

        ref = strs[0]

        for i in range(len(ref)) :
            isit = False
            for k in strs :
                if i < len(k) :
                    if k[i] == ref[i] :
                        pass 
                    else :
                        return ans
                else :
                    return ans
            ans = ans + ref[i]

        return ans 
                        
        