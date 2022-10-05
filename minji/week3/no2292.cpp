//
// Created by 김민지 on 2022/10/05.
//
#include "iostream"
using namespace std;

int main() {
    int n, i;
    cin >> n;

    if (n == 1) {
        cout << 1;
        return 0;
    }
    for (i = 0; n > 1; i++) {
        n -= 6 * i;
    }

    cout << i;
    return 0;
}

//int main(void) {
//    int num = 0, temp = 1;
//    int count = 0;
//
//    cin >> num;
//
//    for (count = 1; temp < num; count++) {
//        temp += 6*count;
//    }
//
//    cout << count;
//}
