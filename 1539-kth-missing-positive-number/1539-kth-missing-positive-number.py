class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        def ismiss(i):
            return arr[i] - (i+1)
        l = 0
        r = len(arr)-1
        while l<=r:
            mid = l+(r-l)//2
            if ismiss(mid)<k:
                l=mid+1
            else:
                r = mid-1
        return l+k
