#204. Count Primes
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        
        # Initially assume all numbers < n are prime
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        # Mark multiples of each prime starting from 2
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n, i):
                    is_prime[j] = False
        
        # Count primes
        return sum(is_prime)
