class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # pointer to s
        j = 0  # pointer to t
        n = len(t)
        m = len(s)
        while j < n and i < m:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == m
