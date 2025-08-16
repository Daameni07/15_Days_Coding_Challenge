#455. Assign Cookies
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i = j = 0
        content = 0
        
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:   # cookie satisfies this child
                content += 1
                i += 1
                j += 1
            else:
                j += 1         # cookie too small, try next one
        
        return content
