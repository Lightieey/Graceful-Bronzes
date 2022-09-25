//
// Created by 김민지 on 2022/09/24.
//
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    if (a > 0 && b > 0)
        cout << 1;
    else if (a < 0 && b > 0)
        cout << 2;
    else if (a < 0 && b < 0)
        cout << 3;
    else if (a > 0 && b < 0)
        cout << 4;
}