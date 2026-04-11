//
// Created by kzatorski on 4/11/26.
//

#include <vector>
#include <algorithm>

class Solution {
public:
    int hIndex(std::vector<int> &citations) {
        int hIdx = 0;
        std::sort(citations.begin(), citations.end(), std::greater<>()); // sort an array in descending order
        for (int i = 0; i < citations.size(); i++) {
            if (hIdx < i + 1 && citations[i] >= i + 1) {
                hIdx = i + 1;
            }
        }

        return hIdx;
    }
};
