class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // 最直接的想法，直接sort取 nums[size - k]
        sort(nums.begin(), nums.end());
        int size = nums.size();
        return nums[size - k];
    }
};
