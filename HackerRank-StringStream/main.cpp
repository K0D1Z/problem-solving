//
// Created by kzatorski on 4/11/26.
//

#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str) {
    istringstream ss(str);
    vector<int> result;

    string a;

    while(std::getline(ss, a, ',')) {
        result.push_back(stoi(a));
    }

    return result;
}

int main() {
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for(int i = 0; i < integers.size(); i++) {
        cout << integers[i] << "\n";
    }

    return 0;
}