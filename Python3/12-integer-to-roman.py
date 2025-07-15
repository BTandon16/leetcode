class Solution:
    def intToRoman(self, num: int) -> str:
        s = ""
        while (num != 0):
            if (num >= 1000):
                s = s + "M"
                num -= 1000
            elif (num >= 500):
                if (num >= 900):
                    s = s + "CM"
                    num -= 900
                else:
                    s = s + "D"
                    num -= 500
            elif (num >= 100):
                if (num >= 400):
                    s = s + "CD"
                    num -= 400
                else:
                    s = s + "C"
                    num -= 100
            elif (num >= 50):
                if (num >= 90):
                    s = s + "XC"
                    num -= 90
                else:
                    s = s + "L"
                    num -= 50
            elif (num >= 10):
                if (num >= 40):
                    s = s + "XL"
                    num -= 40
                else: 
                    s = s + "X"
                    num -= 10
            elif (num >= 5):
                if (num >= 9):
                    s = s + "IX"
                    num -= 9
                else:
                    s = s + "V"
                    num -= 5
            else:
                if (num == 4):
                    s = s + "IV"
                    num -= 4
                else:
                    s = s + "I"
                    num -= 1
        return s