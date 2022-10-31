//
// Created by 김민지 on 2022/10/30.
//
#include "iostream"
using namespace std;

int main() {
    int n1, n2;
    cin >> n1 >> n2;

    int max;
    if (n1 > n2) max = n1;
    else max = n2;

    int gcd = 1, lcm = 1;
    for (int i = 2; i <= max; i++) {
        while (n1%i == 0 && n2%i == 0) {
            n1 /= i;
            n2 /= i;
            gcd *= i;
            lcm *= i;
        }
    }
    gcd = gcd * n1 * n2;

    cout << lcm << "\n" << gcd;
}