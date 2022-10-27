//
// Created by 김민지 on 2022/10/26.
//
#include "iostream"
#include "string"
using namespace std;

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        string str;
        cin >> str;

        bool flag = 1;
        int l = 0;
        for (int r = str.length()-1; l < r; l++, r--) {
            if(str[l] != str[r]) {
                flag = 0;
                break;
            }
        }

        cout << flag  << " " << l + 1 << "\n";
    }
}