class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = nums1+nums2
        merged.sort()
        n = len(merged)
        mid = 0
        if n%2==1:
           
            return merged[n//2]
        else:
            return (merged[n//2-1]+merged[n//2])/2.0

