class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # ans = 0
        # for i in range(len(prices)) :
        #     for j in range(i + 1, len(prices)) :
        #         ans = max(ans , prices[j] - prices[i])

        # return ans

        if len(prices) == 1 :
            return 0 
        mini = prices[0]
        maxi = 0 
        for i in range(1,len(prices)) :
            if prices[i] < mini :
                mini = prices[i]
            diff = 0 if prices[i] - mini < 0 else prices[i] - mini
            maxi = max(diff,maxi)
        return maxi 

        