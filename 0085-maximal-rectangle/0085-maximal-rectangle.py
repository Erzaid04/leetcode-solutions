class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        heights = [0] * len(matrix[0])
        ans = 0

        def hist(heights):
            # your LeetCode 84 code here
            stack = []
            ans = 0
    
            heights.append(0)
    
            for i in range(len(heights)):
                h = heights[i]
    
                while stack and heights[stack[-1]] > h:
                    idx = stack.pop()
    
                    if stack:
                        width = i - stack[-1] - 1
                    else:
                        width = i
    
                    area = heights[idx] * width
                    ans = max(ans, area)
    
                stack.append(i)
    
            return ans

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            # now heights represents this row's histogram
            ans = max(ans, hist(heights))

        return ans