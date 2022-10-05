//
// Created by 김민지 on 2022/10/05.
//
#include "iostream"
using namespace std;

int main() {
    int a, b, c, res;
    cin >> a >> b >> c;

    if (b >= c) {
        cout << -1;
    } else {
        res = a / (c - b);
        cout << res + 1;
    }
}