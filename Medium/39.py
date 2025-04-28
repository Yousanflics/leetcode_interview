# Combination Sum

def combinationSum(candidates, target):
    res = []
    # 递归函数，如果target 被 - 到 0 直接 return 并且把 path 添加到 res 结果中，这个也是递归终止环节
    def backtrack(start, target, path):
        if target == 0:
            res.append(path)
            return
        #逐个遍历整个 candidates 数组的每一个元素，如果这个元素比要求和的 target 还要大的话那就直接 continue 继续下面的循环
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
            # 否则就继续递归 target 减去当前 target 的操作，并且 start 变成了 i
            # 因为数字可以重复使用所以是 i 开始，如果不允许重复那就是要 i + 1
            backtrack(i, target - candidates[i], path + [candidates[i]])

    backtrack(0, target, [])
    return res
