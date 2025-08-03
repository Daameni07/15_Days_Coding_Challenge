#125.valid-palindrome
#https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        return (lambda c: c == c[::-1])(''.join(ch.lower() for ch in s if ch.isalnum()))
