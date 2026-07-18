class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num > 0:
                seen.add(num)
        for i in range(len(nums)+1):
            if i+1 not in seen:
                return i+1

            
        