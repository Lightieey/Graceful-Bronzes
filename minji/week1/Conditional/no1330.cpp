//
// Created by 김민지 on 2022/09/24.
//
#include <iostream>
using namespace std;

int main() {
    int a = 0, b = 0;
    cin >> a >> b;
    if (a > b)
        cout << ">";
    else if (a < b)
        cout << "<";
    else
        cout << "==";
}