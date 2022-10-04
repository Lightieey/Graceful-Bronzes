//
// Created by 김민지 on 2022/09/23.
//

#include "iostream"
using namespace std;

int main(void) {
    int num[] = {};
    int max = 0;
    int idx = 0;

    for (int i = 0; i < 9; i++) {
        cin >> num[i];
        if (num[i] > max) {
            max = num[i];
            idx = i;
        }
    }

    cout << max << endl;
    cout << idx + 1;

    return 0;
}