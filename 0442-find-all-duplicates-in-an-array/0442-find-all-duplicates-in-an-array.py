class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        for num,count in freq.items():
            if count ==2:
                ans.append(num)
        return ans