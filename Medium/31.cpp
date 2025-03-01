/*
寻找给定 nums 的 next permutation(排列) 

代码思路：

- 找到需要调整的位置：
    从数组的右边开始，找到第一个升序对，即满足 num[i] < num[i+1] 的 i。
     
    1 2 7 4 3 1

    1 3 1 2 4 7

    2 跟 3(从右往左第一个比2大的元素跟 2 交换) 然后在转折点的的右边 reverse

    这个位置的 num[i] 是我们需要调整的地方，称为 "转折点"。如果整个数组是降序排列（nums[i] > nums[i+1]）（没有找到升序对），说明已经是字典序最大排列，需要直接将数组翻转为最小排列。

    1 1 2 3 4 7 

- 找到需要交换的元素：

    在 i 的右侧（从右到左）找到第一个比 num[i] 大的数 num[j]。交换 num[i] 和 num[j]，以确保调整后的排列比当前排列更大。
    调整后部分的排列：

    由于 i 右侧部分是降序排列的，交换后需要将其反转为升序排列，从而确保是最小的字典序排列。
    特殊情况：

    如果遍历到最后都没有找到升序对，直接将整个数组反转为升序排列（因为已经是字典序最大的排列）。

时间复杂度：O（n）
空间复杂度：O（1）

std：reverse, swap, c++ sort 可以直接按照字典序排序
*/

class Solution {
public:
    void nextPermutation(vector<int> & nums) {
        int i, j, n = nums.size();
        for(i = n - 2; i >= 0; --i) {
            // 找到了转折点，如果是 3 2 1 则找不到顺序则直接调到 reverse 这个步骤从头到位直接 reverse
            if(nums[i + 1] > nums[i]) {
                for(j = n - 1; j > i; --j){
                    if(nums[j] > nums[i]) break; //在 i 右侧部分（nums[i+1] 到 nums[n-1]），从右往左找第一个比 nums[i] 大的数 nums[j]。因为此时 i 的右边都是逆序 5 4 3 2 1 这样，例如 i 的下一个是 5， i 是 2，则 i 当前样子是 3 2 5 4 3 2 1
                }
                swap(nums[i], nums[j]);
                reverse(nums.begin() + i + 1, nums.end());
                return;
            }
        }
        //从右到左都没有找到顺序则说明当前是完整的逆序则全部转置拿到的是最小的字典序
        reverse(nums.begin(), nums.end());
    }
};
