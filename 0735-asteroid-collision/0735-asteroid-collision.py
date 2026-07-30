class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for num in asteroids:
            alive = True

            while stack and stack[-1] > 0 and num < 0:

                
                if stack[-1] <-num:
                    stack.pop()
                    continue

               
                elif stack[-1] == -num:
                    stack.pop()
                    alive = False
                    break

               
                else:
                    alive = False
                    break

            if alive:
                stack.append(num)

        return stack