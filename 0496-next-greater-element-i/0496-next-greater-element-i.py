class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums1)):
            found = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    for k in range(j+1,len(nums2)):
                        if nums1[i]<nums2[k]:
                            ans.append(nums2[k])
                            found = True
                            break
                    break
            if not found:
                ans.append(-1)

                       
        return ans

        