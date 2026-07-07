class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_idx = {}
        for i,ch in enumerate(s):
            last_idx[ch] = i
        start = 0
        end = 0
        ans = []
        for i,ch in enumerate(s):
            end = max(end,last_idx[ch])

            if i == end:
                ans.append(end - start + 1)
                start = end+1
        return ans

        