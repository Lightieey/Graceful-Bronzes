//
// Created by 김민지 on 2022/10/17.
// flag++ flag-- 해서 확인하는거 서치함
//
#include "iostream"
using namespace std;

int main() {
    int flag = 0;
    int num;
    for (int i = 0; i < 8; i++) {
        cin >> num;
        if (num-1 == i) flag++;
        else if (num-1 == 7-i) flag--;
    }

    if (flag == 8) cout << "ascending";
    else if (flag == -8) cout << "descending";
    else cout << "mixed";

    return 0;
}