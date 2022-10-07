//
// Created by 김민지 on 2022/10/06.
//

#include "iostream"
using namespace std;

int main() {
    int t, h, w, n;
    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> h >> w >> n;

        int floor, room;
        if (n % h == 0) {
            floor = h;
            room = n / h;
        } else {
            floor = n % h;
            room = (n / h) + 1;
        }

        if (room < 10) cout << floor << "0" << room << endl;
        else cout << floor << room << endl;
    }
}

//#include <iostream>
//using namespace std;
//
//int main() {
//    int t;
//    int h, w, n;
//    int result;
//    cin >> t;
//
//    for (int i = 0; i < t; i++) {
//        cin >> h >> w >> n;
//
//        if (n%h == 0) {
//            result = h * 100 + (n / h);
//        }
//        else {
//            result = (n%h) * 100 + (n / h) + 1;
//        }
//        cout << result << endl;
//    }
//}
