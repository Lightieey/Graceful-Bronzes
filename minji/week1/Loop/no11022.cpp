//
// Created by 김민지 on 2022/09/24.
//
#include <iostream>
using namespace std;

int main() {
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);

    int t, a, b;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> a >> b;
        cout << "Case #" << i + 1 << ": " << a << " + " << b << " = " << a + b << "\n";
    }
}