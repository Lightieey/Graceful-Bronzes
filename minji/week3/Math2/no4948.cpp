//
// Created by 김민지 on 2022/10/08.
//
#include "iostream"
#include "cmath"
using namespace std;

int main() {
    int n;

    while (cin >> n) {
        if (!n) break;

        bool isPrime[2*n+1];
        fill_n(isPrime, 2*n+1, true);

        isPrime[0] = false; isPrime[1] = false;

        for (int i = 2; i <= sqrt(2*n); i++) {
            if (isPrime[i]) {
                for (int j = i*2; j <= 2*n; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        int sum = 0;
        for (int i = n + 1; i <= 2*n; i++) {
            if (isPrime[i]) {
                sum += 1;
            }
        }

        cout << sum << "\n";
    }
}