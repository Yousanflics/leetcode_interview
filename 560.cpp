/*
560. Subarray Sum Equals K
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

求和为 k 的连续子数组的个数
市面上比较推崇的解法：通过 HashMap 建立连续子数组的和与它出现次数之间的映射，开始加入 { 0, 1 } why? 因为当前思路是便利数组中的数据用 sum 记录到当前位置的累加和，建立 HashMap 的目的是为了可以更快的查找 sum-k 是否存在即是否有连续子数组的和是 sum-k，如果 HashMap 中事先没有 m[0] 的话这个符合题意的结果就无法累加到结果 res 中故为什么需要在初始化中加入 { 0, 1 }

子数组的和可以通过前缀和计算：
假设前缀和 sum[i] 表示从数组开头到第 i 个元素的和。子数组从 j 到 i 的和可以表示为：
sum[i] - sum[j - 1], 如果 j = 0，则子数组和直接是 sum[i]
问题转化：
找和为 k 的子数组，等价于找 sum[j-1] = sum[i] - k

快速判断是否存在满足条件的前缀和：
    存储前缀和及其出现次数，可以快速判断是否存在一个之前的前缀和等于 
        sum[i]−k。
    这种方法避免了每次检查是否存在符合条件的前缀和时，都从头遍历数组，从而将时间复杂度降低到 
        O(n)。
支持子数组的动态增长：
    前缀和记录的是累积和，随着数组的遍历不断更新，可以动态判断是否存在符合条件的子数组。
    直接存储每个元素出现的次数无法提供这种累积和信息。
当前前缀和计算：
nums = {3, 4, 5};
k = 7;
sum[0] = 3
sum[1] = 3 + 4 = 7
sum[2] = 7 + 5 = 12

如何通过 m[sum - k] 判断子数组的存在？
核心思想：前缀和的差值
假设当前前缀和为 sum，要寻找一个子数组使得其和为 k。

如果存在一个之前的前缀和 sum_prev，使得：
sum - sum_prev = k
则从 sum_prev 到当前 sum 的这段子数组的和就是 
k
转化为代码：
sum_prev = sum - k
检查 sum_prev 是否存在于哈希表 m 中：
在 m 中就会得到 1 不在就会得到 0
res += m[sum - k];

Extra:
如果不同 index 的前缀和想同也没有关系因为加入 0 在最后的集合中那也是相当于新的子数组

暴力的时间复杂度是 O（N^2）当前的时间复杂度使用了前缀和这个tricks之后是 O（N）

*/
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int res = 0; sum = 0; n = nums.size();
        unordered_map<int, int> m {{0, 1}};
        for(int i = 0; i < n; i++){
            // 逐渐累加从而记录到当前 i 的前缀和
            sum += nums[i];
            // 通过判断 m[sum - k] 是否有值即存在之前的子数组和等于 k
            res += m[sum-k];
            ++m[sum];
        }
        return res;
    }
};
