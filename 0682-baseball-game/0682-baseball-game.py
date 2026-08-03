class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ch in operations:
            if ch != "C" and ch!= "D" and ch!= "+":
                stack.append(int(ch))
        
            if ch == "C":
                stack.pop()
            elif ch == "D":
                mul = (stack[-1])*2
                stack.append(mul)
            elif ch == "+":
                
                stack.append(stack[-1] + stack[-2])
        ans = sum(stack)
        return ans