//
// Created by 김민지 on 2022/11/18.
//
#include "iostream"
using namespace std;

// 1->3 | 4->1 | 2->4 | 3->2
int main() {
    int k, max_x = 0, max_y = 0, dif_x = 500, dif_y = 500;
    cin >> k;

    int dir[6][2] = {0,};

    for (int i = 0; i < 6; i++) {
        cin >> dir[i][0] >> dir[i][1];
        if (dir[i][0] <= 2) {
            if (dir[i][1] > max_x) max_x = dir[i][1];
        } else {
            if (dir[i][1] > max_y) max_y = dir[i][1];
        }
    }

    for (int j = 0, i = 1; j < 6; j++, i++) {
        i %= 6;
        if ((dir[j][0] == 1 && dir[i][0] == 3) || (dir[j][0] == 4 && dir[i][0] == 1) ||
            (dir[j][0] == 2 && dir[i][0] == 4) || (dir[j][0] == 3 && dir[i][0] == 2)) {
            dif_x = dir[j][1];
            dif_y = dir[i][1];
        }
    }

    cout << (max_x * max_y - dif_x * dif_y) * k;
}