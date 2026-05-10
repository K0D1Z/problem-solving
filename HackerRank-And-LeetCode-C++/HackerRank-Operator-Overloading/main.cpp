//
// Created by kzatorski on 4/29/26.
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


class Matrix {
public:
    vector<vector<int>> a;
};

Matrix operator+(Matrix& m1, Matrix& m2) {
    Matrix result;
    // if (m1.a.size() != m2.a.size()) {return result;}
    for (int i = 0; i < m1.a.size(); i++) {
        vector<int> row;
        for (int j = 0; j < m1.a[0].size(); j++) {
            int temp = m1.a[i][j] + m2.a[i][j];
            row.push_back(temp);
        }
        result.a.push_back(row);
    }
    return result;
}



int main () {
    int cases,k;
    cin >> cases;
    for(k=0;k<cases;k++) {
        Matrix x;
        Matrix y;
        Matrix result;
        int n,m,i,j;
        cin >> n >> m;
        for(i=0;i<n;i++) {
            vector<int> b;
            int num;
            for(j=0;j<m;j++) {
                cin >> num;
                b.push_back(num);
            }
            x.a.push_back(b);
        }
        for(i=0;i<n;i++) {
            vector<int> b;
            int num;
            for(j=0;j<m;j++) {
                cin >> num;
                b.push_back(num);
            }
            y.a.push_back(b);
        }
        result = x+y;
        for(i=0;i<n;i++) {
            for(j=0;j<m;j++) {
                cout << result.a[i][j] << " ";
            }
            cout << endl;
        }
    }
    return 0;
}
