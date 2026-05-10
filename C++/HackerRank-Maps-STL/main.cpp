//
// Created by kzatorski on 4/28/26.
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
using namespace std;


int main() {
    int Q;
    cin >> Q;
    map<string, int> m;
    for (int i = 0; i <= Q; i++) {
        int query;
        char name[100];
        int mark;

        int a, b, c = 0;
        char buf[100];

        fgets(buf, sizeof(buf), stdin);
        sscanf(buf, "%d %s %d", &query, &name, &mark);


        string strName = name;
        if (query == 1) {
            if (m.count(strName)) {
                m.at(strName) += mark;
            }
            else {
                m.insert(make_pair(strName, mark));
            }
        }
        else if (query == 2) {
            if (m.count(strName)) {
                m.erase(strName);
            }
        }
        else if (query == 3) {
            if (m.count(strName)) {
                cout << m.at(strName) << endl;
            }
            else {
                cout << "0" << endl;
            }
        }
    }
    return 0;
}
