//
// Created by 김민지 on 2022/11/18.
//
#include "iostream"
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int x, y, z;
    while (true) {
        cin >> x >> y >> z;
        if (!x && !y && !z) break;
        if (x*x + y*y == z*z || y*y + z*z == x*x || x*x + z*z == y*y)
            cout << "right" << "\n";
        else cout << "wrong" << "\n";
    }
}