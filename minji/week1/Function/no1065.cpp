//
// Created by 김민지 on 2022/09/24.
//

#include "iostream"
using namespace std;

int count_check(int num) {
    int cnt = 0;
    if (num < 100) {
        return num;
    }
    else {
        cnt = 99;
        for (int i = 100; i <= num; i++) {
            int hun = i / 100;	// 백의 자릿수
            int ten = (i / 10) % 10;	// 십의 자릿수
            int one = i % 10;

            if((hun - ten) == (ten - one)){	// 각 자릿수가 수열을 이루면
                cnt++;
            }
        }
    }

    return cnt;
}

int main() {
    int N;
    cin >> N;
    cout << count_check(N);
}