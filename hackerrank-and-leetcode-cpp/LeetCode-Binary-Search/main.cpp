//
// Created by konrad on 3/11/26.
//

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int leftIndex = 0;
        int rightIndex = nums.size() - 1;
        while (leftIndex <= rightIndex) {
            int middleIndex = (leftIndex + rightIndex) / 2;
            if (nums[middleIndex] < target) {
                leftIndex = middleIndex + 1;
            }
            else if (nums[middleIndex] > target) {
                rightIndex = middleIndex - 1;
            }
            else {
                return middleIndex;
            }
        }
        return -1;
    }
};