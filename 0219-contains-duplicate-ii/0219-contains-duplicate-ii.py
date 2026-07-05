class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        window = set()
        l = 0
        for r in range(len(nums)):
            if nums[r] in window:
                return True
            window.add(nums[r])
            if (r - l)>=k:
                window.remove(nums[l])
                l+=1
        return False
