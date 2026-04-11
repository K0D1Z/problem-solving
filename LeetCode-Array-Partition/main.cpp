//
// Created by kzatorski on 4/11/26.
//

#include <algorithm>
#include <vector>

class Solution {
public:
    int arrayPairSum(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int maxSum = 0;
        for (int i = 0; i < nums.size(); i+= 2) {
            maxSum += nums[i];
        }
        return maxSum;
    }
};