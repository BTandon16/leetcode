class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Solution could be faster
        
        commonPrefLen = len(strs[0])
        for i in range(1, len(strs)):
            for j in range(0, commonPrefLen):
                if (j >= len(strs[i])  or strs[0][j] != strs[i][j]):
                    commonPrefLen = j
                    break
            if (commonPrefLen == 0):
                return ""
        return strs[0][0:commonPrefLen]