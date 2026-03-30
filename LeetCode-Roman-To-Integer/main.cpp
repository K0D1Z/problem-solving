//
// Created by kzatorski on 3/30/26.
//

#include <algorithm>
#include <map>
#include <string>


class Solution {
public:

    int romanToInt(std::string s)
    {
        int sum = 0;

        std::map<char, int> valuesMap = {{'I', 1}, {'V', 5}, {'X', 10},  {'L', 50}, {'C', 100}, {'D', 500}, {'M', 1000}};


        if (s.size() == 0) {
            return 0;
        }

        reverse(s.begin(), s.end());

        sum += valuesMap[s[0]];

        for (int i = 1; i < s.length(); i++) {
            sum += valuesMap[s[i]];
            if (s[i] == 'I') {
                if (s[i-1] == 'V' || s[i-1] == 'X') {
                    sum -= 2*valuesMap[s[i]];
                }
            }
            else if  (s[i] == 'X') {
                if (s[i-1] == 'L' || s[i-1] == 'C') {
                    sum -= 2* valuesMap[s[i]];
                }
            }
            else if  (s[i] == 'C') {
                if (s[i-1] == 'D' || s[i-1] == 'M') {
                    sum -= 2*valuesMap[s[i]];
                }
            }
        }
        return sum;
    }
};
