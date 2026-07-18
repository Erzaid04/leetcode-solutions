class Solution:
    import math 
    def findGCD(self, nums: List[int]) -> int:
        smallest = nums[0]
        largest = nums[0]
        for num in nums:
            if num<smallest:
                smallest = num
            if num >largest:
                largest = num
        return math.gcd(smallest,largest)
        