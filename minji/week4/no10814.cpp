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

    vector<pair<int, pair<int, string>>> members;
    for (int i = 0; i < n; i++) {
        int age;
        string name;
        cin >> age >> name;

        members.push_back(make_pair(age, make_pair(i, name)));
    }

    sort(members.begin(), members.end());
    for (int i = 0; i < n; i++) {
        cout << members[i].first << " " << members[i].second.second << "\n";
    }
}