class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordLen = 0
        for i in range(len(s) - 1, -1, -1):
            if (s[i] == ' '):
                if (wordLen != 0):
                    return wordLen
            else:
                wordLen += 1
        return wordLen