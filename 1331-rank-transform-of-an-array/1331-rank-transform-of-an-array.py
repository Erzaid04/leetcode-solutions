class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        arr1 = sorted(set(arr))

        rank = {}
        for i in range(len(arr1)):
            rank[arr1[i]]= i+1
        ans = []
        for num in arr:
            ans.append(rank[num])
        return ans
            
            
    
