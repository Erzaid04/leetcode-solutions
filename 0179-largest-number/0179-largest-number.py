from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(a,b):
            a = str(a)
            b = str(b)
            if a + b > b + a:
                return -1
            elif a+b < b + a:
                return 1
            else:
                return 0
        nums.sort(key=cmp_to_key(compare))

        result = "".join(map(str, nums))
        if nums[0] == 0:
            return "0"
        return result