//
// Created by 김민지 on 2022/10/17.
//
#include "iostream"
using namespace std;

int main() {
    int a, b, c;
    cin >> a >> b >> c;

    int count[10] = {};

    string res = to_string(a*b*c);
    for (int i = 0; i < res.length(); i++) {
        count[res[i] - '0']++;
    }

    for (int i = 0; i < 10; i++) {
        cout << count[i] << "\n";
    }

    return 0;
}