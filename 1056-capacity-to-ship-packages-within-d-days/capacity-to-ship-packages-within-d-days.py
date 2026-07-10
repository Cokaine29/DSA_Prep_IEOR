class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l = max(weights)
        r = sum(weights) 

        ans = r 

        def canShip(cap) :
            ships = 1 
            count = 1
            curr = 0
            for w in weights :
                if curr + w <= cap :
                    curr += w 
                else :
                    curr = w 
                    count += 1

            if count <= days :
                return True
            else :
                return False

        while l <= r :
            cap = (l+r) // 2 
            if canShip(cap) :
                ans = min(ans, cap)
                r = cap - 1
            else :
                l = cap + 1 

        return ans
        