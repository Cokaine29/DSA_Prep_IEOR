class Solution:
    def frequencySort(self, s: str) -> str:

        m = [[0,None]for _ in range(256)] 
        for c in s :
            print(ord(c))
            m[ord(c)][0] += 1 
            m[ord(c)][1] = c 
        m.sort(reverse = True)

        ans = ""
        for ele in m :
            if ele[0] == 0 :
                break
            else :
                t = ele[1] * ele[0]  
                ans += t 
        return ans

        