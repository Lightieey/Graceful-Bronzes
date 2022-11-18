//
// Created by 김민지 on 2022/11/14.
//
#include "iostream"
#include "vector"
#include "string"
#include "map"
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    map<string, int> poketmon;
    string poketmon_name[n];
    for (int i = 0; i < n; i++) {
        string temp;
        cin >> temp;
        poketmon.insert({temp, i});
        poketmon_name[i] = temp;
    }

    for (int i = 0; i < m; i++) {
        string name;
        cin >> name;
        if (name[0] >= 65 && name[0] <= 90) {
            cout << poketmon[name]+1 << "\n";
        } else {
            cout << poketmon_name[stoi(name)-1] << "\n";
        }
    }
}