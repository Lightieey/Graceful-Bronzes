//
// Created by 김민지 on 2022/10/29.
//
#include "iostream"
using namespace std;

int main() {
    int nums[9][9] = {0,};

    int max = 0, maxi = 0, maxj = 0;
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cin >> nums[i][j];
            if (nums[i][j] > max) {
                max = nums[i][j];
                maxi = i;
                maxj = j;
            }
        }
    }

    cout << max << "\n" << maxi+1 << " " << maxj+1;
}