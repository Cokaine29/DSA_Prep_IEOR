class Solution:
    def countGoodNumbers(self, n: int) -> int:

        # if n % 2 == 0 :
        #     return (20**(n//2)) % (10**9 + 7)
        # else :
        #     return (5 * 20**((n - 1) //2)) % (10**9 + 7)
        MOD = 10**9 + 7 
        if n == 1 :
            return 5 

        else :
            even = (n + 1) // 2
            odd = n // 2 
            return (pow(5,even,MOD) * pow(4,odd,MOD)) % MOD