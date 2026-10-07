class Solution:
    def climbStairs(self, n: int) -> int:

        dp = {}

        def fun(i) :
            if i == n :
                return 1 
            elif i > n :
                return 0 
            if i in dp :
                return dp[i]
            one = fun(i+1)
            two = fun(i+2)
            dp[i] = one + two
            return one + two

        return fun(0)

        