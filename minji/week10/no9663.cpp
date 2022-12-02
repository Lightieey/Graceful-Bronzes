//
// Created by 김민지 on 2022/12/02.
//
#include "iostream"
#define MAX 15
using namespace std;

int n;
int Qcount = 0;
int board[MAX] = {0,};

int promising(int cnt) {
    for (int i = 0; i < cnt; i++) {
        if (board[i] == board[cnt] || abs(board[i] - board[cnt]) == cnt - i)
            return 0;
    }
    return 1;
}

void nQueen(int cnt) {
    if (cnt == n) {
        Qcount++;
        return;
    }

    for (int i = 0; i < n; i++) {
        board[cnt] = i; // 안괜찮으면 다음 for문에서 덮어써짐

        if (promising(cnt)) {   // 괜찮으면 다음 수행
            nQueen(cnt+1);
        }
    }
}

int main() {
    cin >> n;
    nQueen(0);
    cout << Qcount;
}