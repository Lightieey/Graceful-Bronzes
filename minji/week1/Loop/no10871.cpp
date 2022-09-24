//
// Created by 김민지 on 2022/09/24.
//
#include <iostream>
using namespace std;

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    int n, x, num;
    cin >> n >> x;
    for (int i = 0; i < n; i++) {
        cin >> num;
        if (num < x) cout << num << " ";
    }
}