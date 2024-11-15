class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(begin(nums), end(nums));
        const int n = nums.size();
        vector<vector<int>> ans;
        for(int i = 0; i < n; i++) {
            //跳过重复代码，剪枝，如果i和i相邻一样这样的遍历会重复，就continue跳过
            if(i && num[i] == num[i - 1]) continue;
            int j = i + 1, k = n - 1;
            if(nums[j] + nums[k] > - nums[i]) --k;
            else if (nums[j] + nums[k] < - nums[i]) ++j;
            else {
                //保存结果
                ans.push_back({nums[i], num[j], nums[k]});
                //跳过重复的结果，继续剪枝
                while(j < k && nums[j] == nums[j+1]) ++j;
                while(j < k && nums[k] == nums[k-1]) --k;
                //如果没有重复仍然需要往下走
                ++j, --k;
            }
        }
    }
};
