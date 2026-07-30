class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}

    
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1

        sorted_freq = sorted(freq.values(), reverse=True)

        ans = 0

        
        for i, f in enumerate(sorted_freq):
            cost = (i // 8) + 1
            ans += f * cost

        return ans