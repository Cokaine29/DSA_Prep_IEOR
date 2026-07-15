class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) == len(needle) :
            return 0 if haystack == needle else -1 

        i = 0 
        j = len(needle) - 1 

        while i <= len(haystack) - len(needle)  :
            if haystack[i:j+1] == needle :
                return i 
            i += 1 
            j += 1 
            
        return -1 

