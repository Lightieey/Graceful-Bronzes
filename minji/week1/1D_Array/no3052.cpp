//
// Created by 김민지 on 2022/09/24.
// 서치함
#include <iostream>
using namespace std;

int main(void) {
    int count[42] = {};
    int n;

    for(int i = 0; i < 11; i++) {
        cin >> n;
        count[n % 42]++;
    }

    int result = 0;
    for(int n : count) {
        if (n > 0) result++;
    }

    cout << result;

    return 0;
}