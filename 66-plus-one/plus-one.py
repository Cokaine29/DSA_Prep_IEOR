class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1) :
            if digits[i] < 9 :
                digits[i] = digits[i] + carry 
                return digits
            else :
                digits[i] = 0
                carry = 1 
        return [1] + [0] * len(digits)
        