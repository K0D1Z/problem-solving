//
// Created by kzatorski on 4/28/26.
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    int Q;
    cin >> Q;
    set<int> s;
    for (int i = 0; i < Q; i++) {
        int query, number;
        cin >> query;
        cin >> number;
        if (query == 1) {
            s.insert(number);
        }
        if (query == 2) {
            if (s.find(number) != s.end()) {
                s.erase(number);
            }
        }
        if (query == 3) {
            if (s.find(number) != s.end()) {
                cout << "Yes" << endl;
            }
            else {
                cout << "No" << endl;
            }
        }
    }



    return 0;
}



