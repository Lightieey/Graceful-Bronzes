//
// Created by 김민지 on 2022/11/25.
//
#include "iostream"
#include "vector"
#include "algorithm"
using namespace std;

int GCD(int a, int b) {
    if (a % b == 0) return b;
    else return GCD(b, a % b);
}

int main() {

    int n;
    cin >> n;

    int nums[n];
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    sort(nums, nums+n);

    int gcd = nums[1] - nums[0];
    for (int j = 2; j < n; j++) {
        gcd = GCD(gcd, nums[j] - nums[j-1]);
    }

    vector<int> res;
    for (int i = 2; i*i <= gcd; i++) {
        if (gcd % i == 0) {
            res.push_back(i);
            if (i != gcd / i) res.push_back(gcd / i);
        }
    }
    res.push_back(gcd);
    sort(res.begin(), res.end());

    for (int i : res)
        cout << i << " ";



}