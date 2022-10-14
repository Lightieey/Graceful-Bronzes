//
// Created by 김민지 on 2022/10/15.
//
#include "iostream"
#include "algorithm"
#include "vector"
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;

    vector<int> nums;
    int onums[n];
    for (int i = 0; i < n; i++) {
        int num;
        cin >> num;
        onums[i] = num;
        nums.push_back(num);
    }

    sort(nums.begin(), nums.end());
    nums.erase(unique(nums.begin(), nums.end()), nums.end());

    // lower_bound : 찾고자 하는 숫자 이상인 숫자가 처음으로 나오는 위치 인덱스 반환
    for (int i = 0; i < n; i++) {
        cout << lower_bound(nums.begin(), nums.end(), onums[i]) - nums.begin() << " ";
    }
}