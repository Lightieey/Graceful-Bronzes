//
// Created by 김민지 on 2022/11/04.
//
#include "iostream"
#include "string"
using namespace std;

int main() {
    int n;
    cin >> n;

    int nums[10000] = {0,};

    int num = 666;
    for (int i = 0; i < 10000; num++){
        if (to_string(num).find("666") != string::npos) {
            nums[i++] = num;
        }
    }

    cout << nums[n-1];
}