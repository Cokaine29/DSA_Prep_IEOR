class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for i in s :
            if i.isalnum():
                cleaned += i.lower()
        def palindrome(i,s) :
            if len(s) == 0 or len(s) == 1 :
                return True
            if i >= len(s) // 2 :
                return True
            if s[i] != s[len(s)-i-1] :
                return False
            return palindrome(i+1,s)
        return palindrome(0,cleaned)


        
        