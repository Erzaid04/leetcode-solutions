class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        window_length = 0
        freq = {}
        longest = 0
        max_freq = 0
        l = 0
        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]]+=1
            else:
                freq[s[r]] = 1
            window_length = r - l + 1
            max_freq = max(max_freq,freq[s[r]])
            replacement = window_length - max_freq
            while replacement>k:
                freq[s[l]]-=1
                l+=1
                window_length = r - l + 1
                replacement = window_length - max_freq
            longest = max(window_length,longest)
        return longest