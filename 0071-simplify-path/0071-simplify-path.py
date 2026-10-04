class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        path = [s for s in path if s]
        stack = []
        for s in path:
            if s == "..":
                if stack:
                    stack.pop()
            elif s == ".":
                continue
            else:
                stack.append(s)

        if stack:
            res = ""
            for i in stack:
                res += "/" + i
            return res
        else:
            return "/"
        