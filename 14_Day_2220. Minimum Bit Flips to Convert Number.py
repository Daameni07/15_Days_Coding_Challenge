#2220. Minimum Bit Flips to Convert Number
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR finds differing bits
        diff = start ^ goal
        # Count the number of 1s (bit flips needed)
        return bin(diff).count('1')
