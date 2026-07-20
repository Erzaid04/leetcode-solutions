class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        total= sum(nums[:k])
        max_sum = total
        n = len(nums)
        for r in range(k,n):
            total+=nums[r]
            total-=nums[r-k]
            max_sum = max(max_sum, total)
        return max_sum/k


