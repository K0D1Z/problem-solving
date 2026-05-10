//
// Created by konrad on 3/11/26.
//

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        size_t arr_len = nums.size();
        map<int, int> duplicateMap;

        for (int i = 0; i < arr_len; i++) {
            if (duplicateMap.count(nums[i])) {
                return true;
            }
            duplicateMap[nums[i]] = 0;
        }
        return false;
    }
};