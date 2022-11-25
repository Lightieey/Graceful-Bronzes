//
// Created by 김민지 on 2022/11/25.
//
#include "iostream"
using namespace std;

int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n-1);
}

int main() {
    int n, k;
    cin >> n >> k;

    cout << factorial(n) / (factorial(n-k) * factorial(k));
}