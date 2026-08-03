class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            else:
                if not stack:
                    return False

                if ch == ")"  and stack[-1] == "(":
                    stack.pop()
                
                elif ch == "}" and stack[-1] == "{":
                    stack.pop()
                elif ch == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False

        if len(stack)!= 0:
            return False
        return True