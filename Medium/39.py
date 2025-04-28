# Combination Sum

def combinationSum(candidates, target):
    res = []
    def backtrack(start, target, path):
        if target == 0:
            res.append(path)
            return
        #
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
            backtrack(i, target - candidates[i], path + [candidates[i]])

    backtrack(0, target, [])
    return res
