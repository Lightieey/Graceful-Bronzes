//
// Created by 김민지 on 2022/10/05.
//
#include "iostream"
#include "cmath"
using namespace std;

int main() {
    int a, b, v;
    cin >> a >> b >> v;

// time over
//    int i = 0;
//    while(true) {
//        i++;
//        v -= a;
//        if (v <= 0) break;
//        v += b;
//    }

    cout<<fixed;
    cout.precision(0);
    cout << ceil((double)(v-a)/(a-b)) + 1;
}