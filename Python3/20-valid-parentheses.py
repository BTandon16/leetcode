class Solution:
    def isValid(self, s: str) -> bool:
        # Approach: Two pointers
        # Left pointer gets the open bracket, right gets the closed
        # Check for correct bracket type

        # (){}[]
        # ({[]})
        # ({})[]
        openChars = ['(', '[', '{']
        closeChars = [')', ']', '}']
        
        openStackArr = []
        for i in range(len(s)):
            if s[i] in openChars:
                openStackArr.append(s[i])
            else:
                if openStackArr == []:
                    return False
                
                # Using .index probably increases runtime a lot compared to just checking the 3 brackets directly
                if closeChars.index(s[i]) == openChars.index(openStackArr[len(openStackArr) - 1]):
                    openStackArr.pop()
                else:
                    return False
        
        if openStackArr == []:
            return True
        else:
            return False

s = Solution()
print(s.isValid("(())[{}]{}[]"))