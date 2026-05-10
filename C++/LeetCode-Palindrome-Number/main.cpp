#include <stack>

//
// Created by kzatorski on 3/30/26.
//

// class Solution {
// public:
//     bool isPalindrome(int x) {
//         if (x < 0) { return false;}
//         std::stack<int> numStack;
//         int xCopy = x;
//         while (x != 0) {
//             numStack.push(x % 10);
//             x /= 10;
//         }
//         while (!numStack.empty()) {
//             int num = xCopy % 10;
//             xCopy /= 10;
//             auto x = numStack.top();
//             numStack.pop();
//             if (num != x) return false;
//         }
//         return true;
//     }
// };

class Solution {
public:
    bool isPalindrome(int x) {

        if (x < 0 || (x % 10 == 0 && x != 0)) return false;

        int reversed = 0;


        while (x > reversed) {
            reversed = reversed * 10 + x % 10;
            x /= 10;
        }

        return (x == reversed) || (x == reversed / 10);
    }
};