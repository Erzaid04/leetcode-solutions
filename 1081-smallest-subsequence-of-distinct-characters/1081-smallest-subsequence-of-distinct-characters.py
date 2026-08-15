class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        freq = {}
        seen = set()
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
        for ch in s:
            freq[ch]-=1
            if ch in seen:
                continue
            while stack and stack[-1]>ch and freq[stack[-1]]>0:
                x = stack.pop()
                seen.remove(x)
            stack.append(ch)
            seen.add(ch)
        return "".join(stack)