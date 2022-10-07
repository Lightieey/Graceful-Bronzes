//
// Created by 김민지 on 2022/10/08.
//
#include "iostream"
#include "cmath"
using namespace std;

int main() {
    int t, n;
    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> n;

        bool isPrime[n+1];
        fill_n(isPrime, n+1, true);

        isPrime[0] = false, isPrime[1] = false;

        for (int i = 2; i <= sqrt(n); i++) {
            if (isPrime[i]) {
                for (int j = i*2; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
        }

        int min = 0;
        for (int i = 2; i < n; i++) {
            if (isPrime[i] && isPrime[n-i]) {
                if (n-2*i >= 0 && n-2*i < n-2*min) {
                    min = i;
                }
            }
        }

        cout << min << " " << n-min << "\n";
    }
}

/**
 * 서치함
 * <stdio.h>로 시간 단축
 * 에라토스테네스의 체를 문제 최대 수인 10000 + 1 사이즈로 미리 만들어 놓고 사용!
 * 나는 매번 입력 받을 때마다 새로 만들어서 시간이 오래 걸린 것...
 */
//#include <stdio.h>
//int main(void) {
//    int t, n;
//    bool num[10002];
//    for (int i = 0; i <= 10001; i++) {
//        num[i] = true;
//    }
//    num[1] = false;
//    for (int i = 2; i * i <= 10001; i++) {
//        if (num[i]) {
//            for (int j = i * i; j <= 10001; j += i) {
//                num[j] = false;
//            }
//        }
//    }
//    scanf("%d", &t);
//    while (t--) {
//        scanf("%d", &n);
//        //두 소수의 차이가 가장 작게 나는 경우는 n값의 절반인 경우에 해당됨
//        //n/2값을 시작으로 조사한다.
//        for (int i = n / 2; i > 0; i--) {
//            if (num[i] && num[n - i]) {
//                printf("%d %d\n", i, n - i);
//                break;
//            }
//        }
//    }
//    return 0;
//}

