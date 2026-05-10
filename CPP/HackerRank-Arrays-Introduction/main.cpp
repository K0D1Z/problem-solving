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
    reverse(v.begin(), v.end());

    for (const auto& i : v) {
        cout << i << " ";
    }
    return 0;
}
