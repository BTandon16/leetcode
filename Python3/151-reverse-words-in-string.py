class Solution:
    def reverseWords(self, s: str) -> str:
        # Shows null??
        # word = ""
        # reverse = ""
        # for i in range(len(s) - 1, -1, -1):
        #     if (reverse != "" and word != "" and s[i] == " "):
        #         reverse = reverse + word + " "
        #         word = ""
        #     elif (s[i] != " "):
        #         word = s[i] + word
        #         if (word != "" and i == 0):
        #             reverse = reverse + word
        # if (reverse[len(reverse) - 1] == " "):
        #     return reverse[0:len(reverse) - 1]
        # return reverse

        words = s.split()
        res = ""
        for i in range(len(words)):
            if (i != len(words) - 1):
                res = res + words[len(words) - 1 - i] + " "
            else:
                res = res + words[len(words) - 1 - i]
        return res