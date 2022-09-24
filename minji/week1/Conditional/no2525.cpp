//
// Created by 김민지 on 2022/09/23.
//

#include "iostream"
using namespace std;

int main(void) {
    int h, m, r;
    cin >> h >> m;
    cin >> r;

    m += r;
    h += m / 60;

    m %= 60;
    h %= 24;

    cout << h << " " << m;

}