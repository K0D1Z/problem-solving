//
// Created by konrad on 3/11/26.
//
#include <vector>
#include <map>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int>& nums, int target)
    {
        map<int, int> numMap;

        for (int i = 0; i < nums.size(); i++)
        {
            int complement = target - nums[i];
            if (numMap.count(complement) == 1)
            {
                return {numMap[complement], i};
            }

            numMap[nums[i]] = i;
        }

        return {};
    }
};
