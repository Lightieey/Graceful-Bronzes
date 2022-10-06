//
// Created by 김민지 on 2022/10/06.
// 서치함. 재귀함수 쓰기 별표 ****
//
#include "iostream"
using namespace std;

int getNum(int k, int n) {
    if (n == 1)
        return 1;
    if (k == 0)
        return n;
    return (getNum(k-1, n) + getNum(k, n-1));
}

int main() {
    int t, k, n;
    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> k >> n;
        cout << getNum(k, n) << endl;
    }
}