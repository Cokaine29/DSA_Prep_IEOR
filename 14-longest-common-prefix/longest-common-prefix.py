class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        ## Approach 1 
        # ans = ""

        # ref = strs[0]

        # for i in range(len(ref)) :
        #     isit = False
        #     for k in strs :
        #         if i < len(k) :
        #             if k[i] == ref[i] :
        #                 pass 
        #             else :
        #                 return ans
        #         else :
        #             return ans
        #     ans = ans + ref[i]

        # return ans 
                        

        ## Approach 2 

        if len(strs) == 1 :
            return strs[0]
        strs.sort()
        ans = ""
        f = strs[0]
        l = strs[-1]

        for i in range(min(len(f),len(l))) :
            if f[i] == l[i] :
                ans += f[i]
            else :
                return ans
        return ans

        
        