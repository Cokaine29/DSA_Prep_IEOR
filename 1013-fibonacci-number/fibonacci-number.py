class Solution:
    def fib(self, n: int) -> int:

        dp = {}

        def fun(n) :
            if n == 0 or n == 1 :
                return n 
            if n in dp :
                return dp[n]
            else :
                ans = fun(n-1) + fun(n-2)
                dp[n] = ans
                return ans

        return fun(n)

        