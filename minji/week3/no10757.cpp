//
// Created by 김민지 on 2022/10/07.
//
#include "iostream"
#include "vector"
using namespace std;

int main() {
    string a, b;
    cin >> a >> b;

    vector<char> A,B,res;
    for (int i = 0; i < a.length(); i++) {
        A.push_back(a[i]);
    }
    for (int i = 0; i < b.length(); i++) {
        B.push_back(b[i]);
    }

    int ta = 0, tb = 0, c = 0;
    while(!A.empty() || !B.empty()) {

        if (A.empty()) ta = 0;
        else {
            ta = A.back() - '0';
            A.pop_back();
        }

        if (B.empty()) tb = 0;
        else {
            tb = B.back() - '0';
            B.pop_back();
        }

        res.push_back(((ta + tb + c) % 10) + '0');

        if (ta + tb + c > 9) c = 1; // 이전 캐리어 값 확인
        else c = 0;
    }

    if (c) res.push_back('1');

    while (!res.empty()) {
        cout << res.back();
        res.pop_back();
    }

}