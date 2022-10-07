//
// Created by 김민지 on 2022/10/07.
//
#include "iostream"
using namespace std;

int main() {
    int n, temp;
    cin >> n;

    temp = n;
    for (int i = 0; temp > 0; i++) {
        temp = n;
        temp -= 3 * i;
        if (temp % 5 == 0) {
            cout << temp / 5 + i;
            return 0;
        }
    }
    cout << -1;
    return 0;
}