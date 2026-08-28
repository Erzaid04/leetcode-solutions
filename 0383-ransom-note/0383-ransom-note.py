class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = {}

        for ch in magazine:
            cnt[ch] = cnt.get(ch, 0) + 1

        for ch in ransomNote:
            if cnt.get(ch, 0) == 0:
                return False
            cnt[ch] -= 1

        return True