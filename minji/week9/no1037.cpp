//
// Created by 김민지 on 2022/11/25.
//
#include "iostream"
using namespace std;

int main() {
    int n;
    cin >> n;

    int min = 1000000, max = 0;
    while (n--) {
        int temp;
        cin >> temp;
        if (min > temp) min = temp;
        if (max < temp) max = temp;
    }
    cout << min * max;
}