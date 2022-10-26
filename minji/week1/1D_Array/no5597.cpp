//
// Created by 김민지 on 2022/10/26.
//
#include "iostream"
using namespace std;

int main() {
    bool nums[30] = {0,};

    for (int i = 0; i < 28; i++) {
        int num;
        cin >> num;
        nums[num-1] = 1;
    }

    for (int i = 0; i < 30; i++) {
        if (!nums[i])
            cout << i+1 << "\n";
    }
}