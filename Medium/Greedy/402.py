# remove k digits
# 其实这题最好的思路是用单调栈，而且很好解决
class Solution:
    def removeKdigits(self, num:str, k:int) -> str:
        stack = []
        for digit in num:
            # 还有得减少(k > 0),栈不为空,栈顶元素比现在遇到的大就需要pop，因为是求最小，那么遇到的大的就要pop出来
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k > 0:
            stack.pop()
            k -= 1
        
        result = ''.join(stack).lstrip('0')
        return result if result else '0'
