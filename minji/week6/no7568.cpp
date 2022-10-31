//
// Created by 김민지 on 2022/10/31.
//
#include "iostream"
using namespace std;

int main() {
    int n;
    cin >> n;

    int persons[n][2];
    for (int i = 0; i < n; i++) {
        cin >> persons[i][0] >> persons[i][1];
    }

    for (int i = 0; i < n; i++) {
        int rank = 0;
        for (int j = 0; j < n; j++) {
            if (persons[i][0] < persons[j][0] && persons[i][1] < persons[j][1])
                rank++;
        }
        cout << rank+1 << " ";
    }

    return 0;
}