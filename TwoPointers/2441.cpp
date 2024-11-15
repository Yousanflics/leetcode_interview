class Solution {
public:
    int findMaxK(vector<int>& nums) {
        sort(begin(nums), end(nums), [](int a, int b) { 
            return abs(a) == abs(b) ? a < b : abs(a) > abs(b);
            });
        for(int i = 1; i < nums.size(); i++) {
            if(nums[i] == - nums[i - 1]) return nums[i];
        }
        return -1;
    }
};
