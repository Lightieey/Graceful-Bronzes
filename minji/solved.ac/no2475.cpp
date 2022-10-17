//
// Created by 김민지 on 2022/10/17.
//
#include "iostream"
using namespace std;

int main() {
    int num, sum = 0;
    for (int i = 0; i < 5; i++) {
        cin >> num;
        sum += num * num;
    }

    cout << sum % 10;
}