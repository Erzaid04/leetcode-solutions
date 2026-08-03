class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st1= []
        st2 = []

        for ch in s:
            if ch!= "#":
                st1.append(ch)
            else:
                if len(st1)!=0:
                    st1.pop()
        for ch in t:
            if ch!= "#":
                st2.append(ch)
            else:
                if len(st2)!=0:
                    st2.pop()
        if st1 != st2:
            return False
        return True
