/*
入门级找简单状态转移方程 DP，题目说从 grid 左上到右下寻找最小 path sum
*/

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int row = grid.size(), col = grid[0].size();
        for(int i = 0; i < row; ++i) {
            for(int j = 0; j < col; ++ j) {
                if(i == 0 && j == 0) continue;
                int up = (i == 0) ? INT_MAX : grid[i - 1][j];
                int left = (j == 0) ? INT_MAX : grid[i][j - 1];
                grid[i][j] += min(up, left);
            }
        }
        // grid 的最后一个元素，也就是右下的那个
        return grid.back().back();
    }
};
