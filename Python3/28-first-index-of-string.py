class Solution:
    def strStr(self, haystack: str, needle: str) -> int:     
        passed = 0
        if (len(needle) > len(haystack)):
            return -1

        for i in range(len(haystack)):
            if (len(needle) > len(haystack) - i):
                return -1
            
            if haystack[i] == needle[0]:
                if (len(needle) == 1):
                    return i
                for j in range(1, len(needle)):
                    if haystack[i + j] != needle[j]:
                        passed = 0
                        break
                    if (j == len(needle) - 1):
                        passed = 1
                
                if (passed == 1):
                    return i
        return -1