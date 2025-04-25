# asteroid collision
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            # 向右移动
            if asteroid > 0 or not stack:
                stack.append(asteroid)
                continue
            # 向左移动
            while True:
                if not stack:
                    stack.append(asteroid)
                    break
                if stack[-1] < 0:
                    stack.append(asteroid)
                    break
                # 栈顶向右
                if stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                if stack[-1] == abs(asteroid):
                    stack.pop()
                    break
                # 栈顶的更大，当前的 asteroid 爆炸
                break
        return stack
    
    def asteroidCollision1(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            #针对每一个asteroid去标记的
            will_survive = True
            while will_survive and stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] > -asteroid:
                    will_survive = False
                elif stack[-1] == -asteroid:
                    will_survive = False
                    stack.pop()
                else:
                    stack.pop()
            if will_survive:
                stack.append(asteroid)
        return stack

