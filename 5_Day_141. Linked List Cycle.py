#141. Linked List Cycle
#https://leetcode.com/problems/linked-list-cycle/
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next          # Move slow by 1 step
            fast = fast.next.next     # Move fast by 2 steps

            if slow == fast:
                return True           # Cycle detected

        return False                  # No cycle
