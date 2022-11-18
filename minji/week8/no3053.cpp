//
// Created by 김민지 on 2022/11/18.
//
#include "iostream"
#include "cmath"
using namespace std;

int main() {
    int r;
    cin >> r;

    cout << fixed;
    cout.precision(6);

    cout << round(r*r*M_PI * 1000000)/1000000 << "\n";
    cout << (double)r*r*2 << "\n";
}