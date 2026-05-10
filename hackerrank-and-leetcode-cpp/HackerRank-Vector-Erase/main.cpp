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
    int N;
    cin >> N;
    vector<int> v;
    int temp;
    for (int i = 0; i < N; i++) {
        cin >> temp;
        v.push_back(temp);
    }
    int n1, n2, n3;
    cin >> n1;
    cin >> n2;
    cin >> n3;

    v.erase(v.begin() + n1-1);
    v.erase(v.begin() + n2-1, v.begin() + n3 -1);
    cout << v.size() << endl;;
    for (const auto& i : v) {
        cout << i << " ";
    }


    return 0;
}
