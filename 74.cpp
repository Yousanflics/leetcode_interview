/*
在排好序的二维数组中进行查找
思路1：
- 二分查找

思路2：
- 双指针，一个从 [0,0] 开始，一个从 [m-1, n-1]开始
这里考虑到二维数组的特别性选择了思路2进行实现
从矩阵的右上角开始搜索，遍历整个矩阵确保 i 在有效的行范围之内(i < m),j在有效列范围之内(j >=0)
- 如果当前元素 matrix[i][j] == target 直接返回 true
- 如果 matrix[i][j] 比 target 要大，说明 target 应该在当前这个值的左边因此 j-- 移动到左边这一列
- 如果 matrix[i][j] 比 target 要小，说明 target 应该在下方，因此 i++ 移动到下一行
- while 循环解说说明遍历完了一整个没有找到，因此这里应该是 return false
*/

// 时间复杂度 O(m+n)
class Solution {
public:
    bool searchMatrix(vector<vector<int>> &matrix, int target) {
        // j 是一行有多少的 count
        int i = 0, j = (int)matrix[0].size() - 1;
        while(i < matrix.size() && j >= 0) {
            if(matrix[i][j] == target) return true;
            if(matrix[i][j] > target) --j;
            else ++i;
        }
        return false;
    }
};
