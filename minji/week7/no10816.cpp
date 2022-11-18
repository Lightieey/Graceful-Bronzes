//
// Created by 김민지 on 2022/11/17.
//
#include "iostream"
#include "map"
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n;

    map<int, int> nums;
    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        nums[temp]++;
        /*if (nums.find(temp) != nums.end())
            nums[temp]++;
        else nums.insert({temp, 1});*/
    }

    cin >> m;
    for (int i = 0; i < m; i++) {
        int num;
        cin >> num;
        cout << nums[num] << " ";
        /*int cnt = 0;
        if (nums.find(num) != nums.end())
            cnt = nums[num];
        cout << cnt << " ";*/
    }
}

/*
#include <iostream>
#include <algorithm>

using namespace std;

int arr[500002];
int N, M, card;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> card;
        arr[i] = card;
    }
    sort(arr, arr + N); // 이분탐색을 위해 오름차순 정렬

    cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> card;
        cout << upper_bound(arr, arr + N, card) - lower_bound(arr, arr + N, card)<<" ";
    }
}*/
