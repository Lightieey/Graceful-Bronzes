//
// Created by 김민지 on 2022/10/14.
//
#include "iostream"
#include "algorithm"
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    int nums[n];
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    sort(nums, nums + n);

    cout << nums[n-k];
}