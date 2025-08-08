#456. 132 Pattern
#https://leetcode.com/problems/132-pattern/
from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        third = float('-inf')  # This represents nums[k]

        # Traverse from right to left
        for num in reversed(nums):
            # If num < third, we found nums[i] < nums[k]
            if num < third:
                return True

            # Update third with the largest possible nums[k]
            while stack and num > stack[-1]:
                third = stack.pop()

            stack.append(num)

        return False
