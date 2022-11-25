//
// Created by 김민지 on 2022/11/26.
//
#include "iostream"
using namespace std;

/*
 * 10이 얼마나 곱해져 있는지 찾는 문제
 * 10! = 10*9*8*7*6*5*4*3*2*1 -> 10, 5, 2
 * => 결국 (2, 5) 쌍이 얼마나 있는지 찾는 문제!
 */

int main() {
    int n;
    cin >> n;

    int cnt2 = 0, cnt5 = 0;
    for (int i = 2; i <= n; i++) {
        int temp = i;
        while (temp % 2 == 0) {
            temp /= 2;
            cnt2++;
        }
        while (temp % 5 == 0) {
            temp /= 5;
            cnt5++;
        }
    }

    if (cnt2 > cnt5) cout << cnt5;
    else cout << cnt2;
}