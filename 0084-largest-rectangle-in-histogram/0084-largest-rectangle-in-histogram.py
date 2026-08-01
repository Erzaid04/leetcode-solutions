class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = []
        maxArea = 0

        for i in range(n + 1):
            h = 0 if i == n else heights[i]

            while st and h < heights[st[-1]]:
                height = heights[st.pop()]
                width = i if not st else i - st[-1] - 1
                maxArea = max(maxArea, height * width)

            st.append(i)

        return maxArea