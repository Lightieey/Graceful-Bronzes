//
// Created by 김민지 on 2022/11/11.
//
#include "iostream"
#include "algorithm"
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    int have[n];
    for (int i = 0; i < n; i++) {
        cin >> have[i];
    }
    sort(have, have+n);

    int m, temp;
    cin >> m;

    for (int i = 0; i < m; i++) {
        cin >> temp;
        cout << binary_search(have, have+n, temp) << " ";
    }

    return 0;
}