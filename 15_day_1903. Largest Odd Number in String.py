#1903. Largest Odd Number in String
class Solution:
    def largestOddNumber(self, num: str) -> str:
        # scan from the end for the last odd digit
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 == 1:   # odd digit found
                return num[:i + 1]
        return ""  # no odd digit found
