//
// Created by konrad on 3/4/26.
//
#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);



int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    if (n == 1)
    {
        std::cout << "one" << std::endl;
    }
    else if (n == 2)
    {
        std::cout << "two" << std::endl;
    }
    else if (n == 3)
    {
        std::cout << "three" << std::endl;
    }
    else if (n == 4)
    {
        std::cout << "four" << std::endl;
    }
    else if (n == 5)
    {
        std::cout << "five" << std::endl;
    }
    else if (n == 6)
    {
        std::cout << "six" << std::endl;
    }
    else if (n == 7)
    {
        std::cout << "seven" << std::endl;
    }
    else if (n == 8)
    {
        std::cout << "eight" << std::endl;
    }
    else if (n == 9)
    {
        std::cout << "nine" << std::endl;
    }
    else {
        std::cout << "Greater than 9" << std::endl;
    }


    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
