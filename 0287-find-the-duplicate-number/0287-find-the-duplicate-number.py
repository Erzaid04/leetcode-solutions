class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = 1
        r = len(nums)-1
        while l<r:
            mid = l+(r-l)//2
            count=0
            for num in nums:
                if num<=mid:
                    count+=1
            if count>mid:
                r = mid
            else:
                l=mid+1
        return l