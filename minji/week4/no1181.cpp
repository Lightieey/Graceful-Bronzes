//
// Created by 김민지 on 2022/10/15.
//
#include "iostream"
#include "algorithm"
#include "vector"
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<pair<int, string>> strings;
    for (int i = 0; i < n; i++) {
        string str;
        cin >> str;
        strings.push_back(make_pair(str.length(), str));
    }

    sort(strings.begin(), strings.end());
    strings.erase(unique(strings.begin(), strings.end()), strings.end());
    for (int i = 0; i < strings.size(); i++) {
        cout << strings[i].second << "\n";
    }
}