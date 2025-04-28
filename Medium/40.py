# Combination Sum II

class Solution:
    def combinationSum2(candidates, target):
        res = []
        # 方便剪枝
        candidates.sort()
        def backtrack(start, target, path):
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target or (i > start and candidates[i] == candidates[i-1]):
                    continue
                backtrack(i+1, target-candidates[i], path + [candidates[i]])
            
        backtrack(0, target, [])
        return res
