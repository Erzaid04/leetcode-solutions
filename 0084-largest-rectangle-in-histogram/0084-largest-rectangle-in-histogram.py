class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        heights.append(0)
        for i in range(len(heights)):
            h = heights[i]
            while stack and heights[stack[-1]]>h:
                idx = stack.pop()
                if stack:
                    width = i - stack[-1] -1 
                else:
                    width = i
                Area = heights[idx] * width
                ans = max(ans,Area)
            stack.append(i)
        return ans
                    


    