# combination of III sum

from typing import List
# 考虑到要遍历所有的结果，backtracking 或者递归，这里是数组的处理考虑前者

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def backtrack(start, path, target):
            if len(path) == k and target == 0:
                res.append(path[:])
                return 
            if len(path) >= k or target < 0:
                return
            for i in range(start, 10):
                path.append(i)
                backtrack(i+1, path, target-i)
                # 返回到上一个位置，树的 dfs 也要 pop
                path.pop()

        backtrack(1, [], n)
        return res

