//
// Created by 김민지 on 2022/10/08.
//
#include "iostream"
#include "cmath"
using namespace std;

int main() {
    int n, num, count;
    cin >> n;

    count = n;
    for (int i = 0; i < n; i++) {
        cin >> num;

        if (num == 1) count--;
        for (int j = 2; j <= sqrt(num); j++){
            if (num % j == 0) {
                count--;
                break;
            }
        }
    }

    cout << count;
    return 0;
}