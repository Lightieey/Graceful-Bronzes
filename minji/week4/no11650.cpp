//
// Created by 김민지 on 2022/10/14.
//
#include "iostream"
#include "vector"
#include "algorithm"
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<vector<int>> coords(n, vector<int>(2,0));
    for (int i = 0; i < n; i++) {
        cin >> coords[i][0] >> coords[i][1];
    }
    sort(coords.begin(), coords.end());

    for (int i = 0; i < n; i++) {
        cout << coords[i][0] << " " << coords[i][1] << "\n";
    }

}