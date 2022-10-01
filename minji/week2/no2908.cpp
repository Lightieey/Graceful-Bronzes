//
// Created by 김민지 on 2022/09/26.
//
#include "iostream"
#include "string"
#include "algorithm"
using namespace std;

int main() {
    string n1, n2;
    cin >> n1 >> n2;

    reverse(n1.begin(), n1.end());
    reverse(n2.begin(), n2.end());

    if (stoi(n1) > stoi(n2)) cout << n1;
    else cout << n2;
}