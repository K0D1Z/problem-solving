//
// Created by kzatorski on 4/28/26.
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int nOfInts;
    int input;
    std::cin >> nOfInts;
    std::vector<int> v;
    while (std::cin >> input) {
        v.push_back(input);
    }
    sort(v.begin(), v.end());

    for (const auto& i : v) {
        std::cout << i << " ";
    }

    return 0;
}
