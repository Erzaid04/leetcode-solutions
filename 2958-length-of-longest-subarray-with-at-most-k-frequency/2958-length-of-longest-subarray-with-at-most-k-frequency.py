class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        length = 0

        for right in range(len(nums)):
            num = nums[right]
            freq[num] = freq.get(num, 0) + 1

            if freq[num] <= k:
                length = max(length, right - left + 1)

            else:
                while freq[num] > k:
                    freq[nums[left]] -= 1
                    left += 1

                length = max(length, right - left + 1)

        return length