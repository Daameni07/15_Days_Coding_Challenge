#234. Palindrome Linked List
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Step 1: Find middle using fast & slow pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        # Step 3: Compare first and second halves
        left, right = head, prev
        while right:  # only need to check right half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
