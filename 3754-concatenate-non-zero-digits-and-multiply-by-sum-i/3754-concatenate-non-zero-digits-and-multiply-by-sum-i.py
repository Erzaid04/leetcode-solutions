class Solution(object):
    def sumAndMultiply(self, n):
        s = str(n)

        digits = []
        digit_sum = 0

        for ch in s:
            if ch != "0":
                digits.append(ch)
                digit_sum += int(ch)

        if not digits:
            return 0

        number = int("".join(digits))
        return number * digit_sum