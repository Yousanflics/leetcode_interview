class Solution {
public:
    //std sort
    int findKthLargest(vector<int>& nums, int k) {
        // 最直接的想法，直接sort取 nums[size - k]
        sort(nums.begin(), nums.end());
        int size = nums.size();
        return nums[size - k];
    }
    // priority queue
    int findKthLargest(vector<int>& nums, int k) {
        // 最直接的想法，直接sort取 nums[size - k]
        priority_queue<int> q(nums.begin(), nums.end());
        // 执行 k - 1 次那现在 top 就是第 k 大的，前面的 k - 1 都是比 k 更大的元素 
        for(int i = 0; i < k - 1, ++ i) {
            q.pop();
        }
        return q.top();
    }

    /*
    如果正好是 k-1，那么直接返回该位置上的数字；如果大于 k-1，说明要求的数字在左半部分，更新右边界，再求新的中枢点位置；反之则更新右半部分，求中枢点的位置
    */
    // 核心思想：快排 Partition，上面的两种方法可以说是有点偷懒，如果不让使用 std 就 gg
    int findKthLargest(vector<int>& nums, int k) {
        int left = 0, right = nums.size() - 1;
        while(true) {
            int pos = partition(nums, left, right);
            if(pos == k - 1) return nums[pos];
            if(pos > k - 1) right = pos - 1;
            else left = pos + 1;
        }
    }
    // 左大右小  big   pivot   small
    int partition(vector<int>& nums, int left, int right) {
        int pivot = nums[left], l = left + 1, r = right;
        while(l <= r) {
            if(nums[l] < pivot && nums[r] > pivot) {
                swap(nums[l++], nums[r--]);
            }
            if(nums[l] >= pivot) ++l;
            if(nums[r] <= pivot) --r;
        }
        // 把 pivot 放到合适的地方即 r 下标的位置
        swap(nums[left], nums[r]);
        return r;
    }
};
