/*
34. Find First and Last Position of Element in Sorted Array
本质是在数组中找到 target 所在的 range
思路: 写一个二分查找的函数，找到当前 target 的 start index，找到 target + 1 的 end index，最后的范围就是 start - （endindex -1）
由于需要 O(logN) 的时间复杂度所以这题的查找最好使用二分查找，binary search，后续可以对 
二分查找进行总结
*/
class Solution {
public:
    vector<int> searchRange(vector<int> & nums, int target) {
        int start = firstGreaterEqual(nums, target);
        if(start == nums.size() || nums[start] != target) return {-1, -1};
        return {start, firstGreaterEqual(nums, target + 1) - 1};
    }

    int firstGreaterEqual(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        while(left < right) {
            int mid = left + (right - left) / 2;
            if(nums[mid] < target) left = mid + 1;
            else right = mid;
        }
        return right;
    }

};


class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int start = firstGreaterEqual(nums, target);
        if (start == nums.size() || nums[start] != target) return {-1, -1};
        return {start, firstGreaterEqual(nums, target + 1) - 1};
    }
    int firstGreaterEqual(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) left = mid + 1;
            else right = mid;
        }
        return right;
    }
};
