//
// Created by 김민지 on 2022/10/26.
//
#include "iostream"
using namespace std;

int pactorial(int n) {
    if (n < 2) return 1;
    return n * pactorial(n-1);
}

int main() {
    int n;
    cin >> n;

    cout << pactorial(n);
}