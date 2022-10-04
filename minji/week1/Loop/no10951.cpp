//
// Created by 김민지 on 2022/09/24.
//
#include <iostream>
using namespace std;

int main() {
    cin.tie(NULL);
    //cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    int a, b;
    while (cin >> a >> b) {
        //if (a == 0 && b == 0) break;
        cout << a + b << "\n";
    }
}