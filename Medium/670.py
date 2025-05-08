class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = [int(d) for d in str(num)]
        n = len(digits)
        
        last = {}
        for i in range(n):
            last[digits[i]] = i
        for i in range(n):
            for d in range(9, digits[i], -1):
                if d in last and digits[d] > i:
                    j = digits[d]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int(''.join(map(str, digits)))
        return num
