/*
如对于题目中给的例子 [1,2,3] 来说，最开始是空集，那么现在要处理1，就在空集上加1，为 [1]，现在有两个子集 [] 和 [1]，下面来处理2，在之前的子集基础上，每个都加个2，可以分别得到 [2]，[1, 2]，那么现在所有的子集合为 [], [1], [2], [1, 2]，同理，处理3的情况可得 [3], [1, 3], [2, 3], [1, 2, 3], 再加上之前的子集就是所有的子集合了
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res(1);// 初始化，包含一个空集合 {{}}

        //
        cout << "Initial res: " << endl;
        printRes(res);
        for(int i  = 0; i < nums.size(); ++i) {
            int size = res.size();
            for(int j = 0; j < size; ++j) {
                res.push_back(res[j]);
                res.back().push_back(nums[i]);
            }
        }
        return res;
    }

    void printRes(vector<vector<int>>& res) {
        cout << "{";
        for(auto & subset: res) {
            cout <<"{";
            for(int num : subset) {
                cout << num << " ";
            }
            cout << "} ";
        }
        cout << "}" <<endl;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {1, 2, 3}; // 测试数据
    vector<vector<int>> res = solution.subsets(nums);

    cout<< "Final subsets result:" <<endl;
    solution.printRes(res);

    return 0;
}
