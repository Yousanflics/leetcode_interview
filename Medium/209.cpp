/*
题目分析：
- 这道题给定了我们一个数字，让求子数组之和大于等于给定值的最小长度，不是等于。
- 跟之前 Maximum Subarray 有些类似，并且我们需要实现 O(n) 和 O(nlgn) 两种解法，
    - O(n) 的实现：定义两个指针 left 和 right，分别记录子数组的左右的边界位置，然后让 right 向右移，直到子数组和大于等于给定值或者 right 达到数组末尾，此时更新最短距离，并且将 left 像右移一位，然后再 sum 中减去移去的值，然后**重复**上面的步骤，直到 right 到达末尾，且 left 到达临界位置，即要么到达边界，要么再往右移动，和就会小于给定值

- 总结
    其实这个算法实现了一个简单的滑动窗口的算法，为了获得窗口内元素和 大于等于 target 元素的最小窗口
*/

// 目前的最快实现
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        if(nums.empty()) return 0;
        // 设置 res = len + 1 就是为了设置为一个不可能的数值，如果遍历了之后还是这个结果那说明没有找到最短的需要返回 0
        int left = 0, right = 0, sum = 0, len = nums.size(), res = len + 1;
        while(right < len) {
            // 先找到一个 right flag，从左到右来一遍，然后接着对左进行缩小，然后进行下一个 right flag
            while(sum < s && right < len) {
                sum += nums[right++];
            }
            while(sum >= s) {
                res = min(res, right - left);
                sum -= nums[left++];
            }
        }
        return res == len + 1 ? 0 : res;
    }
};
