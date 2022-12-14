//
// Created by 김민지 on 2022/10/08.
// 서치함.
// 에라토스테네스의 체 이용 - 기존 방식보다 빠르다..?
//
#include "iostream"
#include "cmath"
using namespace std;

int main() {
    int min, max;
    cin >> min >> max;

    bool isPrime[max+1];
    fill_n(isPrime, max+1, true);

    isPrime[0] = false;
    isPrime[1] = false;

    for (int i = 2; i <=sqrt(max); i++) {
        if (isPrime[i] == true) {
            for (int j = i*2; j <= max; j += i) {
                isPrime[j] = false;
            }
        }
    }

    for (int i = min; i <= max; i++) {
        if (isPrime[i]) cout << i << "\n";
    }

    return 0;
}