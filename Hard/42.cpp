#include <vector>
#include <algorithm>

class Solution {
public:
    int trap(std::vector<int>& height) {
        // If the height vector is empty, no water can be trapped
        // 没有任何高度的话就不能存水
        if (height.empty()) return 0;
        
        int n = height.size(); // Get the size of the height vector
        int left = 0, right = n - 1; // Initialize two pointers, left and right
        int leftMax = 0, rightMax = 0; // Initialize variables to store the maximum heights on both sides
        int waterTrapped = 0; // Initialize the variable to store the total amount of trapped water
        
        // Use two pointers to traverse the height vector from both ends
        while (left < right) {
            if (height[left] < height[right]) {
                // If the current height at the left pointer is less than the height at the right pointer
                if (height[left] >= leftMax) {
                    // Update leftMax if the current height is greater than or equal to leftMax
                    leftMax = height[left];
                } else {
                    // Calculate the trapped water at the current position
                    waterTrapped += leftMax - height[left];
                }
                ++left; // Move the left pointer to the right
            } else {
                // If the current height at the right pointer is less than or equal to the height at the left pointer
                if (height[right] >= rightMax) {
                    // Update rightMax if the current height is greater than or equal to rightMax
                    rightMax = height[right];
                } else {
                    // Calculate the trapped water at the current position
                    waterTrapped += rightMax - height[right];
                }
                --right; // Move the right pointer to the left
            }
        }
        
        return waterTrapped; // Return the total amount of trapped water
    }
};
