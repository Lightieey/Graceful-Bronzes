//
// Created by 김민지 on 2022/10/29.
//
#include "iostream"
using namespace std;

int main() {
    bool paper[101][101] = {0,};

    int n;
    cin >> n;

    int x, y;
    for (int i = 0; i < n; i++) {
        cin >> x >> y;
        for (int xx = x; xx < x+10; xx++) {
            for (int yy = y; yy < y+10; yy++) {
                paper[xx][yy] = 1;
            }
        }
    }

    int count = 0;
    for (int i = 0; i < 101; i++) {
        for (int j = 0; j < 101; j++) {
            if (paper[i][j] == 1) count++;
        }
    }

    cout << count;
}