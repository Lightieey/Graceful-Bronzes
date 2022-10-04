//
// Created by 김민지 on 2022/09/23.
//

#include "iostream"
using namespace std;

int main(void) {
    int total, num;
    int price, count;
    int res = 0;

    cin >> total;
    cin >> num;
    for (int i = 0; i < num; i++){
        cin >> price >> count;
        res += price * count;
    }

    if (res == total) cout << "Yes";
    else cout << "No";
}