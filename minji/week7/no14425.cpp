//
// Created by 김민지 on 2022/11/11.
//
#include "iostream"
#include "vector"
#include "algorithm"
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<string> strs;

    while (n--) {
        string temp;
        cin >> temp;
        strs.push_back(temp);
    }

    sort(strs.begin(), strs.end());
    int count = 0;
    for (int i = 0; i < m; i ++) {
        string temp;
        cin >> temp;


        if (binary_search(strs.begin(), strs.end(), temp)) {
            count++;
        }
    }

    cout << count;

}