//
// Created by kzatorski on 4/11/26.
//

#include <algorithm>
#include <vector>

class Solution {
public:
    int heightChecker(std::pmr::vector<int>& heights) {
        std::vector<int> heightsCopy = heights;
        std::sort(heightsCopy.begin(), heightsCopy.end());
        int output = 0;
        for (int i =0; i < heights.size(); i++) {
            if (heights[i] != heightsCopy[i]) {
                output++;
            }
        }
        return output;
    }
};
