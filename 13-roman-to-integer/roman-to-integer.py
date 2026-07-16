class Solution:
    def romanToInt(self, s: str) -> int:

        # IV IX
        # XL XC
        # CD CM
        count = 0
        d = {
            "I": 1,
            "V": 5,
            "X" : 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        i = 0 
        while i < len(s) :
            if i + 1 < len(s) and s[i:i+2] in d:
                 
                count += d[s[i:i+2]] 
                i += 2 
            else :
                count += d[s[i]]
                i += 1 
        return count
            


