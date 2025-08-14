#1209. Remove All Adjacent Duplicates in String II
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # each element will be [char, count]

        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()  # remove when count reaches k
            else:
                stack.append([ch, 1])

        # reconstruct string
        return "".join(ch * count for ch, count in stack)
