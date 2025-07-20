class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if (len(s) > len(t)):
            return False
        if (len(s) == 0):
            return True
        i = 0
        j = 0
        while i < len(t):
            if (t[i] == s[j]):
                # t = t[i::]
                j += 1
            i += 1
            if (j == len(s)):
                return True
        return False