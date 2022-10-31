//
// Created by 김민지 on 2022/10/29.
//
#include "iostream"
using namespace std;

int main() {
    int n;
    while (cin >> n) {
        if (n == 0) break;

        if (n < 10) cout << "yes\n";
        else if (n < 100) {
            if (n % 11 == 0) cout << "yes\n";
            else cout << "no\n";
        }
        else if (n < 1000) {
            if (n % 10 == (int)(n / 100)) cout << "yes\n";
            else cout << "no\n";
        } else if (n < 10000) {
            if (n % 10 == (int)(n/1000) && (int)(n/10)%10 == ((int)(n/100))%10) cout << "yes\n";
            else cout << "no\n";
        } else {
            if (n % 10 == (int)(n/10000) && (int)(n/10)%10 == ((int)(n/1000))%10) cout << "yes\n";
            else cout << "no\n";
        }
    }
}

#include <iostream>
#include <string>
#include <algorithm> //reverse 함수가 있는 헤더파일

using namespace std;


//int main() {
//    string N;
//
//    while (cin >> N) {
//        if (N=="0") {
//            break;
//        }
//        string buf = N;
//        reverse(N.begin(), N.end()); // 앞 뒤 바꿈
//
//        else if(N == buf) { // 비교
//            cout <<"yes\n";
//        }else {
//            cout <<"no\n";
//        }
//    }
//}

//int main() {
//    string ch;
//    while (1) {
//        cin >> ch;
//        if (ch == "0") { break; }
//        int no = 0;
//        for (int i = 0; i < ch.length() / 2; i++) {
//            if (ch[i] != ch[ch.length() - i - 1]) {
//                no++;	break;
//            }
//        }
//        if (no == 0) { cout << "yes" << endl; }
//        else { cout << "no" << endl; }
//    }
//}
