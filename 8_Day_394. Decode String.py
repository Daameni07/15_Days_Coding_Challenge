#394. Decode String
#https://leetcode.com/problems/decode-string/description/
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # Will store (prev_string, repeat_count)
        current_str = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)  # Build the full number
            elif ch == "[":
                # Push current state and reset
                stack.append((current_str, num))
                current_str = ""
                num = 0
            elif ch == "]":
                # Pop and repeat
                prev_str, repeat_count = stack.pop()
                current_str = prev_str + current_str * repeat_count
            else:
                current_str += ch  # Append letter

        return current_str
