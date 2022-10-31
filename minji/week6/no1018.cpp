//
// Created by 김민지 on 2022/11/01.
//
#include "iostream"
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    char chess[n][m];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> chess[i][j];
        }
    }

    char chess1[8][8] = {
            {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
            {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
            {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
            {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
            {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
            {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
            {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
            {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'}
    };

    char chess2[8][8] = {
            {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
            {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
            {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
            {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
            {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
            {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
            {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
            {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
    };

    int min = n*m;
    for (int i = 0; i <= n-8; i++) {
        for (int j = 0; j <= m-8; j++) {
            int count1 = 0, count2 = 0;

            for (int l = i; l < i+8; l++) {
                for (int k = j; k < j+8; k++) {
                    if (chess[l][k] != chess1[l-i][k-j]) count1++;
                    if (chess[l][k] != chess2[l-i][k-j]) count2++;
                }
            }
            if (min > count1) min = count1;
            if (min > count2) min = count2;
        }
    }

    cout << min;
    return 0;
}