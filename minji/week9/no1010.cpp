//
// Created by 김민지 on 2022/11/25.
//
#include "iostream"
using namespace std;

int main() {
    int N, K;
    long long DP[30][30];

    DP[0][0] = 1;
    DP[1][0] = 1;
    DP[1][1] = 1;

    for (int i = 2; i <= 29; i++)
        for (int j = 0; j <= i; j++)
        {
            if (j == 0) DP[i][0] = 1;
            else if (j == i) DP[i][j] = 1;
            else DP[i][j] = (DP[i - 1][j - 1] + DP[i - 1][j]);
        }

    int t;
    cin >> t;
    while (t--) {
        cin >> N >> K;
        cout << DP[K][N] << "\n";
    }
}