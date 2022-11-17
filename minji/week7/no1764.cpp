//
// Created by 김민지 on 2022/11/17.
//
#include "iostream"
#include "set"
#include "algorithm"
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    set<string> heard;
    set<string> seen;

    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        string temp;
        cin >> temp;
        heard.insert(temp);
    }
    for (int i = 0; i < m; i++) {
        string temp;
        cin >> temp;
        seen.insert(temp);
    }

    set<string> res;
    set_intersection(heard.begin(), heard.end(), seen.begin(), seen.end(), inserter(res, res.begin()));
    cout << res.size() << "\n";
    for (string s : res) {
        cout << s << "\n";
    }
}