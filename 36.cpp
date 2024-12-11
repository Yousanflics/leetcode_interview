/*
验证数独：9*9的每一行每一列都不能有重复的，3*3里面必须包含数字1-9没有重复
最直接的暴力遍历 On^2 是时间复杂度最低的
*/
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<string> st;
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] == '.') continue;
                string t = "(" + to_string(board[i][j] - '0') + ")";
                string row = to_string(i) + t, col = t + to_string(j), cell = to_string(i / 3) + t + to_string(j / 3);
                if (st.count(row) || st.count(col) || st.count(cell)) return false;
                st.insert(row);
                st.insert(col);
                st.insert(cell);
            }
        }
        return true;
    }
};
