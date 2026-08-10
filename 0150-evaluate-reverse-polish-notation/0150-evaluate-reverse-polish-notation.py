class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch.lstrip("-").isdigit():
                stack.append(int(ch))
            else:
                if ch in "*/-+":
                    b = stack.pop()
                    a = stack.pop()
                    if ch == "+":
                        stack.append(a+b)
                    elif ch == "-":
                        stack.append(a-b)
                    elif ch == "*":
                        stack.append(a*b)
                    else:
                        stack.append(int(a/b))
        return stack[-1]

