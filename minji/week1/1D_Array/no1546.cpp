//
// Created by 김민지 on 2022/09/24.
//

#include <iostream>
using namespace std;

int main(void) {
    int N;
    int M = 0;
    double sum = 0;
    int nums[1000] = {};

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> nums[i];
        if (nums[i] > M) M = nums[i];
        sum += nums[i];
    }

    cout << (sum / M * 100) / N;

    return 0;
}