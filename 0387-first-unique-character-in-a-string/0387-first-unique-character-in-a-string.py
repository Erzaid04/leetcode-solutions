class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch] =1

        for i,ch in enumerate(s):
            if freq[ch]==1:
                return i
        return -1
        