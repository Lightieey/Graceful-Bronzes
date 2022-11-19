//
// Created by 김민지 on 2022/11/18.
//
#include "iostream"
using namespace std;

int main() {
    int t;
    cin >> t;
    while (t--) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;

        int n, cnt=0;
        cin >> n;
        while (n--) {
            int cx, cy, r;
            cin >> cx >> cy >> r;

            if ((x1-cx)*(x1-cx)+(y1-cy)*(y1-cy) < r*r)
                if ((x2-cx)*(x2-cx)+(y2-cy)*(y2-cy) > r*r)
                    cnt++;
            if ((x1-cx)*(x1-cx)+(y1-cy)*(y1-cy) > r*r)
                if ((x2-cx)*(x2-cx)+(y2-cy)*(y2-cy) < r*r)
                    cnt++;

        }
        cout << cnt << "\n";
    }
}