//
// Created by 김민지 on 2022/09/24.
//

#include <iostream>
using namespace std;

int main() {
    int a;
    cin >> a;
    if (a < 60)
        cout << "F";
    else if (a < 70)
        cout << "D";
    else if (a < 80)
        cout << "C";
    else if (a < 90)
        cout << "B";
    else
        cout << "A";

}
