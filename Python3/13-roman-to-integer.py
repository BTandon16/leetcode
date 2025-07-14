class Solution:
    def romanToInt(self, s: str) -> int:
        value = 0
        arr = list(s)
        for i in range(len(arr)):
            if arr[i] == "V":
                value += 5
            elif arr[i] == "L":
                value += 50
            elif arr[i] == "D":
                value += 500
            elif arr[i] == "M":
                value += 1000
            elif i == len(arr) - 1:
                if arr[i] == "I":
                        value += 1
                elif arr[i] == "X":
                        value += 10
                elif arr[i] == "C":
                        value += 100
            elif arr[i] == "I":
                if arr[i + 1] == "V" or arr[i + 1] == "X":
                    value -= 1
                else:
                    value += 1
            elif arr[i] == "X":
                if arr[i + 1] == "L" or arr[i + 1] == "C":
                    value -= 10
                else:
                    value += 10
            elif arr[i] == "C":
                if arr[i + 1] == "D" or arr[i + 1] == "M":
                    value -= 100
                else:
                    value += 100
        return value