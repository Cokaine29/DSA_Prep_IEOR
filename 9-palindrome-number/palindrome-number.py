class Solution:
    def isPalindrome(self, x: int) -> bool:
        org = x 
        if x < 0 :
            return False 
        num = 0 
        
        while x > 0 :
            num = num * 10 + x % 10 
            x = x // 10 
        print(num,x)
        return True if org == num else False