class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [int(d) for d in str(num)]
        n = len(digits)
        
        last = {}
        for i in range(n):
            last[digits[i]] = i
        for i in range(n):
            for d in range(9, digits[i], -1):
                #当前找到的最大的在 last 中且 last 位置在 i 的后面 last[d] > i，把 i 和 当前位置换了
                if d in last and last[d] > i:
                    j = last[d]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(map(str, digits)))
        return num
