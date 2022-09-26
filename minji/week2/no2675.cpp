//
// Created by 김민지 on 2022/09/26.
//

#include "iostream"
#include "string"
using namespace std;

int main() {
    int T;
    cin >> T;

    int R;
    string S;
    for (int i = 0; i < T; i++) {
        cin >> R >> S;
        for (int j = 0; j < S.length(); j++) {
            for (int r = 0; r < R; r++) {
                cout << S[j];
            }
        };
        cout << endl;
    }
}