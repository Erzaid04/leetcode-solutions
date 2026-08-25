class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        x = k
        while x in nums:
            x += k
        return x