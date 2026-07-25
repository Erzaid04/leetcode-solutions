class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0)+1
        for ch in t :
            if ch not in freq or freq[ch]==0:
                return ch
            freq[ch]-=1
        