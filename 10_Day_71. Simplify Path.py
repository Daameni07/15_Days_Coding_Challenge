#71. Simplify Path
#https://leetcode.com/problems/simplify-path/description/
class Solution:
    def simplifyPath(self, path: str) -> str:
        # Split by '/' to get path components
        parts = path.split('/')
        stack = []

        for part in parts:
            if part == '' or part == '.':  
                # Skip empty strings or '.' (current directory)
                continue
            elif part == '..':
                # Go up to parent directory if possible
                if stack:
                    stack.pop()
            else:
                # Valid directory name (could be '...', '....', etc.)
                stack.append(part)

        # Join stack into simplified path
        return '/' + '/'.join(stack)
