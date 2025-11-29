class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPalLen = 0
        res_l = 0
        res_r = 0
        
        for i in range(len(s)):
            # Check for Odd Palindrome Lengths
            l = i
            r = i
            while (l >= 0 and r <= len(s) - 1) and (s[l] == s[r]):
                if (maxPalLen < (r - l + 1)):
                    maxPalLen = r - l + 1
                    res_l = l
                    res_r = r
                l -= 1
                r += 1
            
            # Check for Even Palindrome Lengths
            l = i
            r = i + 1
            while (l >= 0 and r <= len(s) - 1) and (s[l] == s[r]):
                if (maxPalLen < (r - l + 1)):
                    maxPalLen = r - l + 1
                    res_l = l
                    res_r = r
                l -= 1
                r += 1
        
        return s[res_l: res_r + 1]

s = Solution()
print(s.longestPalindrome("babadabido"))
print(s.longestPalindrome("cddb"))
            

            
