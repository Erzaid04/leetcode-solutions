class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        best_pal = 0
        idx = 0
        for i in range(n):
            l = i
            r = i
            
            while l >=0 and r<n and s[l] == s[r]:
                if r - l+1 > best_pal:
                    best_pal = max(r-l+1,best_pal)
                    idx = l
                l-=1
                r+=1
            l = i
            r = i + 1
            
            while l >=0 and r<n and s[l] == s[r]:
                if r - l+1 > best_pal:
                    best_pal = max(r-l+1,best_pal)
                    idx = l
                l-=1
                r+=1
        return s[idx:idx + best_pal]
        