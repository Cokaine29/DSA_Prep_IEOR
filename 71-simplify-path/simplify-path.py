class Solution:
    def simplifyPath(self, path: str) -> str:

        items = path.split("/")
        ans = "/"
        stack = []
        for ele in items :
            if ele == "." :
                continue
            elif ele == ".." :
                if stack :
                    stack.pop()
            elif ele == "" :
                continue
            else :
                stack.append(ele)

        return "/" + "/".join(stack)
        

        