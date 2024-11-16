class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while(left <= right) {
            int mid = left + (right - left)/2;
            if(nums[mid] == target) return mid;
            if(nums[left] <= nums[mid]) {
                if(nums[left] <= target && target < nums[mid]) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            } else {
                if(nums[mid] > target && target <= nums[right]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1;
    }
};

/*
1. 在 C++ 中，(right - left) / 2 的结果会向下取整（即取小于或等于计算结果的最大整数），因为整数除法只保留结果的整数部分
2. 二分查找的时间复杂是 O(logN)
3. 部分有序也可以使用二分查找
*/

/*
3,2,1 7,8.9,10, 11, 12, 13
target: 7
1: nums[mid] = 9, nums[left] = 3, nums[right] = 13 mid = 5
2: 0 - 4  nums[left] = 3  nums[right] = 8 mid = 2 nums[mid] = 1
    
*/
