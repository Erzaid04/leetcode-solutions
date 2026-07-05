class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        window = {}
        target = {}
        if len(s1)> len(s2):
            return False
        for ch in s1:
            if ch in target:
                target[ch]+=1
            else:
                target[ch]=1
        for i in range(len(s1)):
            if s2[i] in window:
                window[s2[i]]+=1
            else:
                window[s2[i]]=1
        if window == target:
            return True
        l=0

        for r in range(len(s1),len(s2)):
            if s2[r] in window:
                window[s2[r]]+=1
            else:
                window[s2[r]]=1
            window[s2[l]]-=1

            if window[s2[l]] == 0:
                del window[s2[l]]
            l+=1

            if window == target:
                return True
        return False

        