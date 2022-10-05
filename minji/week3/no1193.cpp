//
// Created by 김민지 on 2022/10/05.
//
#include "iostream"
using namespace std;

int main() {
    int input, sum = 0, i;
    cin >> input;

    for (i = 0; sum < input; i++) {
        sum += i;
    }
    input -= (sum - i + 1);
    if (i % 2 == 0) {
        cout << i - input << "/" << input;
    } else {
        cout << input << "/" << i - input;
    }
    return 0;
}