class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        d = {
            2 : ["a","b","c"],
            3 : ["d", "e", "f"],
            4 : ["g", "h", "i"],
            5 : ["j", "k", "l"],
            6 : ["m", "n", "o"],
            7 : ["p", "q", "r", "s"] ,
            8 : ["t", "u", "v"],
            9 : ["w","x","y","z"]
        }

        def mul(a,b) :
            ans = []
            for i in a :
                for k in b :
                    ans.append(i+k)
            return ans

        if len(digits) == 1 :
            return d[int(digits[0])]
        elif len(digits) == 2 :
            return mul(d[int(digits[0])],d[int(digits[1])])
        elif len(digits) == 3 :
            fh = mul(d[int(digits[0])],d[int(digits[1])])
            return mul(fh,d[int(digits[2])])
        else :
            fh = mul(d[int(digits[0])],d[int(digits[1])])
            sh = mul(d[int(digits[2])],d[int(digits[3])])
            return mul(fh,sh)


