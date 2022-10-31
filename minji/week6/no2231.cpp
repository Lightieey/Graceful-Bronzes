//
// Created by 김민지 on 2022/10/31.
//
#include "iostream"
#include "string"
using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int sum = 0;
        for (char c : to_string(i)) {
            sum += c - '0';
        }
        sum += i;
        if (sum == n) {
            cout << i;
            return 0;
        }
    }
    cout << 0;
    return 0;
}