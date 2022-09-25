//
// Created by 김민지 on 2022/09/24.
//
#include <iostream>
using namespace std;

int main() {
    cin.tie(NULL);
    //cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    int num, count = 0;
    cin >> num;
    int nn = num;
    while (true) {
        nn = ((nn % 10) * 10) + (((nn / 10) + (nn % 10)) % 10);
        count++;
        if (nn == num) break;
    }
    cout << count;
}