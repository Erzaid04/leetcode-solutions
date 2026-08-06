class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        current = n

        while True:
            pro = 1
            temp = current

            while temp > 0:
                digit = temp % 10
                pro *= digit
                temp //= 10

            if pro % t == 0:
                return current

            current += 1