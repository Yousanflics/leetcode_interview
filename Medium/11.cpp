class Solution {
public:
    int maxArea(vector<int>& height) {
        int res = 0, i = 0, j = height.size() - 1;
        while (i < j) {
            int h = min(height[i], height[j]);
            res = max(res, h * (j - i));
            while (i < j && h == height[i]) ++i;
            while (i < j && h == height[j]) --j;
        }
        return res;
    }
};

class Solution {
public:
    int maxArea(vector<int>& height) {
        int res = 0, i = 0, j = height.size() - 1;
        while(i < j) {
            int h  = min(height[i], height[j]);
            res = max(res, h *(j - i));
            //只需要移动最小的那个高度的下标因为最小的决定了最后的面积，++i是为了跳过重复的
            while(i < j && h == height[i]) ++i;
            while(i < j && h == height[j]) --j;
        }
        return res;
    }
};
