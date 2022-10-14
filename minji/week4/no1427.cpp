//
// Created by 김민지 on 2022/10/14.
//
#include "iostream"
#include "algorithm"
using namespace std;

int main() {
    string num;
    cin >> num;

    int nums[num.length()];
    for (int i = 0; i < num.length(); i++) {
        nums[i] = num[i] - '0';
    }

    sort(nums, nums+num.length());
    for (int i = num.length()-1; i > -1; i--) {
        cout << nums[i];
    }
}