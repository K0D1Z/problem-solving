//
// Created by konrad on 3/11/26.
//

#include <algorithm>
#include <cctype>
#include <iostream>
#import <stack>
#include <string>

using namespace std;

class Solution
{
public:
    bool isPalindrome(string s)
    {
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        s.erase(remove_if(s.begin(), s.end(), [](char c) { return !isalnum(c); }), s.end());

        cout << s;
        stack<char> letterStack;
        int i = 0;
        for (; i < (s.length() / 2); i++)
        {
            if (isalnum(s[i]))
            {
                letterStack.push(s[i]);
            }
        }
        if (s.length() % 2 == 1)
        {
            i++;
        }
        for (; i < s.length(); i++)
        {
            if (letterStack.top() == s[i])
            {
                letterStack.pop();
            }
            else
            {
                return false;
            }
        }
        return true;
    }
};

int main()
{
    Solution sol;
    string s = "A man, a plan, a canal: Panama";
    sol.isPalindrome(s);
}
