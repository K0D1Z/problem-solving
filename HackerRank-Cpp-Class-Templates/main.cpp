//
// Created by kzatorski on 4/29/26.
//

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;


template <class T>
class AddElements {
    T arg_;
public:
    AddElements(T arg) : arg_{arg}{};
    T add(T arg2) {
        arg_ += arg2;
        return arg_;
    }
};
template<>
class AddElements<string> {
    string arg_;
public:
    AddElements(string arg) : arg_{arg}{};
    string concatenate(string s) {
        return arg_ + s;
    }
};

int main () {
    int n,i;
    cin >> n;
    for(i=0;i<n;i++) {
        string type;
        cin >> type;
        if(type=="float") {
            double element1,element2;
            cin >> element1 >> element2;
            AddElements<double> myfloat (element1);
            cout << myfloat.add(element2) << endl;
        }
        else if(type == "int") {
            int element1, element2;
            cin >> element1 >> element2;
            AddElements<int> myint (element1);
            cout << myint.add(element2) << endl;
        }
        else if(type == "string") {
            string element1, element2;
            cin >> element1 >> element2;
            AddElements<string> mystring (element1);
            cout << mystring.concatenate(element2) << endl;
        }
    }
    return 0;
}
