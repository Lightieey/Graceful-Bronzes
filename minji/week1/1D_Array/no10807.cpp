//
// Created by 김민지 on 2022/10/26.
//
#include "iostream"
using namespace std;

int main() {
    int n;
    cin >> n;

    int nums[n];
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    int findN;
    cin >> findN;

    n = 0;
    for (int num : nums) {
        if (num == findN) n++;
    }

    cout << n;
}