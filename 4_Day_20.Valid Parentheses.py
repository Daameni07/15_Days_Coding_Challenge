#20. Valid Parentheses
#https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:           
            return False

        pair = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in pair:           
                if not stack or stack.pop() != pair[ch]:
                    return False
            else:                     
                stack.append(ch)

        return not stack               
