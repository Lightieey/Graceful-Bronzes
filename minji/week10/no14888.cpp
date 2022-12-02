//
// Created by 김민지 on 2022/12/03.
//
#include "iostream"
#include "vector"
#include "algorithm"
using namespace std;

int n, m = 0;
int nums[100] = {0,};
int operators[4] = {0,};
int oper_arr[99] = {0,};
vector<int> results;

void dfs(int cnt) {
    if (cnt == m) {
        int res = nums[0];
        for (int i = 0; i < m; i++) {
            switch (oper_arr[i]) {
                case 0:
                    res += nums[i+1];
                    break;
                case 1:
                    res -= nums[i+1];
                    break;
                case 2:
                    res *= nums[i+1];
                    break;
                case 3:
                    res /= nums[i+1];
                    break;
            }
        }
        results.push_back(res);
    }

    for (int i = 0; i < 4; i++) {
        if (operators[i]) {
            operators[i]--;
            oper_arr[cnt] = i;
            dfs(cnt+1);
            operators[i]++;
        }
    }
}

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    for (int i = 0; i < 4; i++) {
        cin >> operators[i];
        m += operators[i];
    }

    dfs(0);

    sort(results.begin(), results.end());
    cout << results[results.size()-1] << "\n" << results[0];
}