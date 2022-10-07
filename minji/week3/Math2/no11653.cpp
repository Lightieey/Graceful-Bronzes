//
// Created by 김민지 on 2022/10/08.
//
#include "iostream"
#include "cmath"
using namespace std;

bool isPrime(int num) {
    if (num == 2) return true;

    bool flag = true;
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) flag = false;
    }

    return flag;
}

int main() {
    int n, temp;
    cin >> n;

    if (n == 1) return 0;

    temp = n;
    for (int i = 2; i <= sqrt(n) + 2; i++) {
        if(isPrime(i)) {
            while (!isPrime(temp) && temp % i == 0) {
                cout << i << endl;
                temp /= i;
            }
            if (isPrime(temp)) {
                cout << temp;
                break;
            }
        }
    }
    return 0;
}