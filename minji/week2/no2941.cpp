//
// Created by 김민지 on 2022/09/30.
//
#include "iostream"
#include "string"
#include "algorithm"
using namespace std;

int main() {
    string str;
    cin >> str;

    string  change[] = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
    int count = 0;
    for (int i = 0; i < 8; i++) {
        while (str.find(change[i]) != string::npos) {
            int idx = str.find(change[i]);
            str.replace(idx, change[i].length(), " ");
            count++;
        }
    }
    str.erase(remove(str.begin(), str.end(), ' '), str.end());
    cout << count + str.length();
    return 0;
}