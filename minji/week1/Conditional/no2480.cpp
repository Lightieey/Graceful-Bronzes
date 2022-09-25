//
// Created by 김민지 on 2022/09/23.
//

#include "iostream"
using namespace std;

int max(int a, int b, int c) {
    int nums[] = {a, b, c};
    int max = nums[0];
    for (int i = 0; i < 3; i++) {
        if (nums[i] > max) max = nums[i];
    }
    return max;
}

int main(void) {
    int d1, d2, d3;
    cin >> d1 >> d2 >> d3;

    if (d1 == d2 && d2 == d3) {
        cout << 10000 + d1*1000;
    }
    else if (d1 == d2 || d2 == d3) {
        cout << 1000 + d2*100;
    }
    else if (d1 == d3) {
        cout << 1000 + d1*100;
    }
    else {
        cout << max(d1,d2,d3) * 100;
    }
}