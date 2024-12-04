import Algorithms

class Solution {
    func countPairs(_ root: TreeNode?, _ distance: Int) -> Int {
        // 初始化返回条件
        var result = 0

        func dfs(_ node: TreeNode?) -> [Int] {
            // 如果节点为空返回 []
            guard let node else {return []}
            // 遍历左边
            let lPath = dfs(node.left)
            // 遍历右边
            let rPath = dfs(node.right)
            // 左右子树长度都是  0 那就是叶子节点，对叶子节点处理并return 1
            guard lPath.count + rPath.count > 0 else { return [1] }
            //
            result += product(lPath, rPath).filter{$0+$1<=distance}.count
            return chain(lPath,rPath).map{$0+1}
        }

        dfs(root!)
        return result
    }
}
