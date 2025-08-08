#
#https://leetcode.com/problems/sliding-window-maximum/
from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices
        res = []

        for i, num in enumerate(nums):
            # 1. Remove smaller values from the back
            while dq and nums[dq[-1]] <= num:
                dq.pop()

            # 2. Add current index
            dq.append(i)

            # 3. Remove leftmost index if out of the window
            if dq[0] <= i - k:
                dq.popleft()

            # 4. Append max for current window
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
