class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        pro = 1
        og = n
        while n > 0:
            digit = n%10
            s+=digit
            pro*=digit
            n//=10
        total = s + pro
        return og%total == 0
