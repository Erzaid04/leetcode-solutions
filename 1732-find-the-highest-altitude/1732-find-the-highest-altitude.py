class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        high = 0

        for x in gain:
            curr+=x
            if curr>high:
                high = curr
        return high