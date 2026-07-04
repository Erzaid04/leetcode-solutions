class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = 0
        max_vowels = 0
        l = 0
        for r in range(len(s)):
            if s[r] in "aeiou":
                vowels+=1
            if r - l + 1 == k:
                max_vowels = max(max_vowels,vowels)
                if s[l] in "aeiou":
                    vowels-=1
                l+=1
        return max_vowels