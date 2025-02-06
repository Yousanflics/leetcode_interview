/*
在排好序的二维数组中进行查找
思路1：
- 二分查找

思路2：
- 双指针，一个从 [0,0] 开始，一个从 [m-1, n-1]开始
这里考虑到二维数组的特别性选择了思路2进行实现
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
