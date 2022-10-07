//
// Created by 김민지 on 2022/10/08.
//
#include "iostream"
#include "cmath"
using namespace std;

int main() {
    int m, n, sum = 0, min;
    cin >> m >> n;

    for (int i = n; i >= m; i--) {

        if (i == 1) break;
        else if (i == 2) {
            sum += 2;
            min = 2;
        }
        else {
            bool flag = true;
            for (int j = 2; j <= sqrt(i); j++) {
                if (i % j == 0) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                cout << i << " ";
                sum += i;
                min = i;
            }
        }
    }

    if (sum == 0) {
        cout << -1;
    } else {
        cout << sum << endl << min;
    }
    return 0;
}