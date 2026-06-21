class Solution:
    def countAndSay(self, n: int) -> str:

        def RLE(s) :
            if len(s) == 1 :
                return "1" + s 
            else :
                stack = []
                ans = ""
                for ele in s :
                    if stack and ele != stack[-1] :
                        ans = ans + str(len(stack)) + stack[-1]
                        stack = []
                    stack.append(ele)
                if stack :
                    ans = ans + str(len(stack)) + stack[-1]

            return ans
        temp = "1"
        for i in range(1, n) :
            ans = RLE(temp)
            temp = ans

        return temp
                    




        