//
// Created by 김민지 on 2022/09/24.
//
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    if (b < 45) {
        b += 15;
        if (a < 1)
            a = 23;
        else
            a -= 1;
    }
    else
        b -= 45;

    cout << a << " " << b << endl;
}