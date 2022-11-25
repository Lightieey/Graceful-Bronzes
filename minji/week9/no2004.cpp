//
// Created by 김민지 on 2022/11/26.
//
#include "iostream"
using namespace std;

long get_cnt2(long n) {
    int cnt = 0;
    while (n >= 2) {
        cnt += n / 2;
        n /= 2;
    }
    return cnt;
}

long get_cnt5(long n) {
    int cnt = 0;
    while (n >= 5) {
        cnt += n / 5;
        n /= 5;
    }
    return cnt;
}

int main() {
    int n, m;
    cin >> n >> m;

    long count2 = get_cnt2(n) - get_cnt2(n-m) - get_cnt2(m);
    long count5 = get_cnt5(n) - get_cnt5(n-m) - get_cnt5(m);

    if (count2 > count5) cout << count5;
    else cout << count2;
}