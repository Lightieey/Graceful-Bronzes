//
// Created by 김민지 on 2022/09/24.
//
#include "iostream"
using namespace std;

int main() {
    int c;
    int n, scores[1000] = {};

    cin >> c;
    for (int i = 0; i < c; i++){
        cin >> n;
        int sum = 0;
        for (int j = 0; j < n; j++) {
            cin >> scores[j];
            sum += scores[j];
        }
        int mean = sum / n;
        int count = 0;
        for (int j = 0; j < n; j++) {
            if (scores[j] > mean) count++;
        }
        cout<<fixed;
        cout.precision(3);
        cout << (double)count / n * 100 << "%" << endl;
    }
}