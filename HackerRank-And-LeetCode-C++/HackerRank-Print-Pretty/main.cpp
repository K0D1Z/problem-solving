//
// Created by kzatorski on 4/28/26.
//

#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int T; cin >> T;
    cout << setiosflags(ios::uppercase);
    cout << setw(0xf) << internal;
    while(T--) {
        double A; cin >> A;
        double B; cin >> B;
        double C; cin >> C;
        // cout << "0x" << std::hex << int(A) << endl;
        // cout  << std::setprecision(2) << B << endl;
        cout << std::dec
             << std::noshowpos
             << std::setfill(' ')
             << std::setw(0)
             << "0x"
             << std::nouppercase
             << std::hex
             << (long long)A << "\n";
        cout << std::dec
             << std::showpos
             << std::fixed
             << std::setprecision(2)
             << std::setfill('_')
             << std::setw(15)
             << std::right
             << B << "\n";
        cout << std::noshowpos
     << std::setfill(' ')
     << std::setw(0)
     << std::uppercase
     << std::scientific
     << std::setprecision(9)
     << C << "\n";
    }
    return 0;

}