//
// Created by 김민지 on 2022/11/25.
//
#include "iostream"
using namespace std;

int GCD(int a, int b) {
    return a % b ? GCD(b, a % b) : b;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int n;
    cin >> n;

    int nums[n];
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    for (int i = 1; i < n; i++) {
        int gcd = GCD(nums[0], nums[i]);
        cout << nums[0]/gcd << "/" << nums[i]/gcd << "\n";
    }
}