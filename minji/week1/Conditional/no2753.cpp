//
// Created by 김민지 on 2022/09/24.
//
#include <iostream>
using namespace std;

int main() {
    int a;
    cin >> a;
    if (a % 400 == 0)
        cout << 1;
    else if (a % 4 == 0 && a % 100 != 0)
        cout << 1;
    else
        cout << 0;

}