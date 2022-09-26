//
// Created by 김민지 on 2022/09/26.
//
#include "iostream"
using namespace std;

int main() {
    string S;
    string alphabet = "abcdefghijklmnopqrstuvwxyz";

    cin >> S;
    for (char c : alphabet) {
        if (S.find(c) != string::npos) {
            cout << S.find(c) << " ";
        }
        else {
            cout << "-1 ";
        }
    }
}