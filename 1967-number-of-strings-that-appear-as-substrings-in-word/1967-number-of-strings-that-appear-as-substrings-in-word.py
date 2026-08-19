class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt = 0
        for pattern in patterns:
            if pattern in word:
                cnt+=1
        return cnt