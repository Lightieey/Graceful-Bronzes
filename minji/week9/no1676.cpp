//
// Created by 김민지 on 2022/11/26.
//
#include "iostream"
using namespace std;

/*
 * 10이 얼마나 곱해져 있는지 찾는 문제
 * 10! = 10*9*8*7*6*5*4*3*2*1 -> 10, 5, 2
 * => 결국 (2, 5) 쌍이 얼마나 있는지 찾는 문제!
 * => 근데, 2는 상대적으로 5보다 많이 들어가게 되어있음!
 * => 그래서 5의 개수만 세도 됨!
 * => 결과적으로 5의 배수의 개수를 찾으면 됨!
 * https://beginnerdeveloper-lit.tistory.com/18
 */

int main() {
    int n;
    cin >> n;

    int res = 0;
    res += n / 5;   // 5의 배수
    res += n / 25;  // 25의 배수
    res += n / 125; // 125의 배수
    cout << res;

    /*int cnt2 = 0, cnt5 = 0;
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
    else cout << cnt2;*/
}