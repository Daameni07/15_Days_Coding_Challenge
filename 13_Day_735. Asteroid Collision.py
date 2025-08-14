#735. Asteroid Collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:  # stack asteroid smaller → pop
                    stack.pop()
                    continue
                elif stack[-1] == -a:  # same size → both explode
                    stack.pop()
                break
            else:
                stack.append(a)

        return stack
