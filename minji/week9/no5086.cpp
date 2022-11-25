//
// Created by 김민지 on 2022/11/25.
//
#include "iostream"
using namespace std;

int main() {
    int n1, n2;
    while (cin >> n1 >> n2) {
        if (!n1 && !n2) break;

        if (n2 % n1 == 0) cout << "factor\n";
        else if (n1 % n2 == 0) cout << "multiple\n";
        else cout << "neither\n";
    }
}