class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        for i in range(min(len(strs[0]), len(strs[len(strs) - 1]))):
            if strs[0][i] != strs[len(strs) - 1][i]:
                if i == 0:
                    return ""
                return strs[0][0 : i]
        return strs[0][0 : min(len(strs[0]), len(strs[len(strs) - 1]))]

