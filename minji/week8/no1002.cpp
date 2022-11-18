//
// Created by 김민지 on 2022/11/18.
//
#include "iostream"
#include "cmath"
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int t, x1, y1, r1, x2, y2, r2;
    cin >> t;
    while (t--) {
        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
        double d = sqrt(pow(x1-x2, 2) + pow(y1-y2, 2));

        if (d == 0) {
            if (r1 == r2) cout << "-1\n";
            else cout << "0\n";
        }
        else if (d > r1 + r2) cout << "0\n";
        else if (d == r1 + r2 || d == abs(r1 - r2)) cout << "1\n";
        else if (d < r1 + r2 && d > abs(r1 - r2)) cout << "2\n";
        else cout << "0\n";
    }
}