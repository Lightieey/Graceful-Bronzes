//
// Created by 김민지 on 2022/10/14.
//
#include "iostream"
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, num;
    cin >> n;

    int counting[10001] = {0,};

    for (int i = 0; i < n; i++) {
        cin >> num;
        counting[num]++;
    }

    for (int i = 0; i < 10001; i++) {
        for (int j = 0; j < counting[i]; j++) {
            cout << i << "\n";
        }
    }
}