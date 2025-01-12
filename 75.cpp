/*
本质上来说还是一道排序题，也是经典的荷兰国旗问题（就地排序）
- 思路
    - 双指针遍历
    - 定义 red 指针指向开头位置，blue 指针指向末尾位置
    - 从开开始便利原数组，如果遇到 0，则交换该值和 red 指针指向的值，并将 red 指针后移一位。若遇到 2，则交换该值和 blue 指针指向的值，并将 blue 指针前移（即 j -- 操作），若遇到 1，则继续遍历
    - 希望达到的效果是 0 都被换到左边了👈🏻，2都被换到👉🏻了

- 问题
    - 为什么 else if 情况下有 nums[i--]
        - 因为交换 nums[i] 和 nums[blue--] 后，nums[i] 位置上的新值可能是 0 或 2，需要重新检查。i-- 保证在下一次循环中不跳过当前位置。
*/

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int red = 0, blue = (int)nums.size() - 1;
        for(int i = 0; i <= blue; ++i) {
            if(nums[i] == 0) {
                swap(nums[i], nums[red++]);
            }else if(nums[i] == 2) {//nums[blue]可以是 0 也可以是 2 所以需要 -- 之后再次跟新的判断一下
                swap(nums[i--], nums[blue--]);
            }
        }
    }
};
