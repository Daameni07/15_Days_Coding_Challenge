#215. Kth Largest Element in an Array
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Min-heap of size k
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)  # push current number
            if len(min_heap) > k:          # keep heap size = k
                heapq.heappop(min_heap)
        
        return min_heap[0]  # root = kth largest
