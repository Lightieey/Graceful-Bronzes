//
// Created by 김민지 on 2022/11/25.
//
#include "iostream"
using namespace std;

int gcd(int a, int b) {
    if (a % b == 0) return b;
    else return gcd(b, a % b);
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int a, b;
        cin >> a >> b;
        cout << a * b / gcd(a, b) << "\n";
    }
}