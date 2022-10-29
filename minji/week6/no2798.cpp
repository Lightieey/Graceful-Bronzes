//
// Created by 김민지 on 2022/10/29.
//
#include "iostream"
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    int nums[n];
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    int max = 0;
    for (int i = 0; i < n-2; i++) {
        for (int j = i+1; j < n-1; j++) {
            for (int l = j+1; l < n; l++) {
                int sum = nums[i] + nums[j] + nums[l];
                if (sum > max && sum <= m) {
                    max = sum;
                }
            }
        }
    }

    cout << max;
}