//
// Created by 김민지 on 2022/09/26.
//
#include "iostream"
using namespace std;

int main() {
    int N = 0, sum = 0;
    string str;

    cin >> N;
    cin >> str;

    for(int i = 0; i < N; i++) {
        sum += str[i] - '0';
    }

    cout << sum;
}