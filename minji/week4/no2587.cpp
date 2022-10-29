//
// Created by 김민지 on 2022/10/29.
//
#include "iostream"
#include "algorithm"
using namespace std;

int main() {
    int num[5] = {};
    int sum = 0;
    for (int i = 0; i < 5; i++) {
        cin >> num[i];
        sum += num[i];
    }

    sort(num, num+5);
    cout << sum/5 << "\n" << num[2];
}