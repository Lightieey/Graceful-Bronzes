//
// Created by 김민지 on 2022/11/17.
//
#include "iostream"
#include "set"
#include "algorithm"
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, temp;
    cin >> n >> m;

    set<int> A, B;
    while (n--) {
        cin >> temp;
        A.insert(temp);
    }
    while (m--) {
        cin >> temp;
        B.insert(temp);
    }

    set<int> res;
    set_difference(A.begin(), A.end(), B.begin(), B.end(), inserter(res, res.begin()));
    set_difference(B.begin(), B.end(), A.begin(), A.end(), inserter(res, res.begin()));

    cout << res.size();
}