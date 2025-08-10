#227. Basic Calculator II
#https://leetcode.com/problems/basic-calculator-ii/description/
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")  # Remove all spaces
        stack = []
        num = 0
        sign = '+'  # Start assuming the first number is positive

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)  # Build the current number
            
            # If it's an operator or the last character, process the number
            if not ch.isdigit() or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] *= num
                elif sign == '/':
                    # Truncate toward zero
                    stack[-1] = int(stack[-1] / num)

                sign = ch
                num = 0

        return sum(stack)
