//
// Created by 김민지 on 2022/11/18.
//
#include "iostream"
#include "set"
using namespace std;

int main() {

    string str;
    cin >> str;

    set<string> arr;
    for (int i = 1; i <= str.length(); i++) {
        for (int j = 0; j <= str.length()-i; j++) {
            arr.insert(str.substr(j, i));
        }
    }
    cout << arr.size();
}