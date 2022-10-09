//
// Created by 김민지 on 2022/10/10.
//
#include "iostream"
#include "algorithm"
using namespace std;

int main() {
    int n;
    cin >> n;

    int nums[n];

    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        nums[i] = num;
    }

    sort(nums, nums + n);

    for (int i = 0; i < n; i++) {
        cout << nums[i] << "\n";
    }
}