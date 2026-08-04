class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nge = {}
        ans = []
        for i in range(len(nums2)):
            while stack and stack[-1]<nums2[i]:
                x = stack.pop()
                num = nums2[i]
                nge[x] = num
            stack.append(nums2[i])
        while stack:
                x = stack.pop()
                nge[x] = -1   


        
        for num in nums1:
            ans.append(nge[num])
        return ans

           