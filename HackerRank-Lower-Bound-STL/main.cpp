//
// Created by kzatorski on 4/29/26.
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int N;
    cin >> N;
    vector<int> v;
    int temp;
    for (int i = 0; i < N; i++) {
        cin >> temp;
        v.push_back(temp);
    }

    int Q;
    cin >> Q;

    for (int i = 0; i < Q; i++) {
        cin >> temp;
        auto low = lower_bound(v.begin(), v.end(), temp);

        if (low != v.end() && *low == temp) {
            cout << "Yes " << (low - v.begin() + 1) << '\n';
        }
        else {
            cout << "No " << (low - v.begin() + 1) << '\n';
        }
    }
    return 0;
}
