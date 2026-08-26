class Solution: 
    def shortestBeautifulSubstring(self, s: str, k: int) -> str: 
        l = 0 
        cnt = 0 
        ans = "" 
 
        for r in range(len(s)): 
            if s[r] == '1': 
                cnt += 1 
 
            # We have k ones 
            while cnt == k: 
                curr = s[l:r+1] 
 
                # Update answer 
                if ans == "" or len(curr) < len(ans) or (len(curr) == len(ans) and curr < ans): 
                    ans = curr 
 
                # Move left 
                if s[l] == '1': 
                    cnt -= 1 
                l += 1 
 
        return ans