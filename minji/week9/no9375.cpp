//
// Created by 김민지 on 2022/11/25.
//
#include "iostream"
#include "map"
using namespace std;

/*
 * type a - 4
 * type b - 5
 * (4+1)C1 * (5+1)C1 - 1
 * 옷 개수 + 옷을 안 입는 경우(1) 더해준 거에서 1개 뽑음.
 * 둘 다 안입은 경우 빼줌.
 */

int main() {
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;
        map<string, int> clothes;
        for (int i = 0; i < n; i++) {
            string name, ctype;
            cin >> name >> ctype;
            clothes[ctype]++;
        }
        int res = 1;
        for (auto i : clothes)
            res *= i.second + 1;
        cout << res - 1 << "\n";
    }
}