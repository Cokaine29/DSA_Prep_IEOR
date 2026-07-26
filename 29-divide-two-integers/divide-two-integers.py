class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        INT_MAX = 2**31 - 1 
        INT_MIN = -1 * 2**31
        
        flag = None
        if (dividend  < 0) ^ (divisor < 0) : 
            flag = -1 
        else :
            flag = 1
        dividend , divisor = abs(dividend) , abs(divisor)
        q = 0
        while dividend >= divisor :
            x = divisor
            p = 0 
            while x <= dividend :
                x = 2 * x 
                if x > dividend :
                    break
                p += 1 
            q += 2**p
            dividend = dividend - divisor * 2**p 
        q = flag * q 

        if q < INT_MIN :
            return INT_MIN
        elif q > INT_MAX :
            return INT_MAX
        return q 

        

        # dividend , divisor = abs(dividend) , abs(divisor)
        # count = 0
        # while dividend >= divisor :
        #     dividend = dividend - divisor
        #     count += 1 
        # count = flag * count
        # if count > INT_MAX :
        #     return INT_MAX
        # elif count < INT_MIN :
        #     return INT_MIN
        # return count 

        


        