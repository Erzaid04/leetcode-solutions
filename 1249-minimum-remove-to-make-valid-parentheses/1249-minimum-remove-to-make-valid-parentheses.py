class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = set()
        for i,ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                if stack:
                    stack.pop()
                else:
                    remove.add(i)
        while stack:
            remove.add(stack.pop())
        ans = []
        for i,ch in enumerate(s):
            if i not in remove:
                ans.append(ch)
        return "".join(ans)
