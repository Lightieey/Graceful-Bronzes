//
// Created by 김민지 on 2022/09/24.
//

#include "iostream"
using namespace std;

int main() {
    int n;
    string s;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> s;

        int score = 0, total = 0;
        for (char c : s) {
            if (c == 'O') {
                score++;
            } else {
                score = 0;
            }
            total += score;
        }

        cout << total << endl;
    }
}