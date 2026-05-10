//
// Created by kzatorski on 4/11/26.
//

// #include <vector>
//
// class Solution {
// public:
//     std::vector<int> smallerNumbersThanCurrent(std::vector<int>& nums) {
//         std::vector<int> output(nums.size());
//         for (int i = 0; i < nums.size(); ++i) {
//             for (int j = 0; j < nums.size(); ++j) {
//                 if (nums[j] < nums[i]) {
//                     output[i]++;
//                 }
//             }
//         }
//         return output;
//     }
// };

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> smallerNumbersThanCurrent(std::vector<int>& nums) {
        std::vector<int> output(nums.size());
        std::vector<int> copy = nums;
        sort(copy.begin(), copy.end());

        for (int i = 0; i < nums.size(); ++i) {
            int j = 0;
            while (copy[j] < nums[i]) {
                output[i]++;
                j++;
            }
        }
        return output;
    }
};