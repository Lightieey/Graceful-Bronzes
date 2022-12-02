//
// Created by 김민지 on 2022/12/03.
//
#include "iostream"
#include "vector"
#include "algorithm"
using namespace std;

int n, m;
int s[21][21] = {0,};
int visited[21] = {0,};
int team_arr[11] = {0,};
vector<int> results;

void dfs(int cnt, int start) {
    if (cnt == m) {
        int res1 = 0;
        for (int i = 0; i < m-1; i++) {
            for (int j = i+1; j < m; j++) {
                res1 += s[team_arr[i]-1][team_arr[j]-1] + s[team_arr[j]-1][team_arr[i]-1];
            }
        }

        vector<int> team_other;
        for (int i = 1; i <= n; i++) {
            bool flag = false;
            for (int num : team_arr) {
                if (num == i) flag = true;
            }
            if (!flag) {
                team_other.push_back(i);
            }
        }

        int res2 = 0;
        for (int i = 0; i < m-1; i++) {
            for (int j = i+1; j < m; j++) {
                res2 += s[team_other[i]-1][team_other[j]-1] + s[team_other[j]-1][team_other[i]-1];
            }
        }

        results.push_back(abs(res1 - res2));
        return;
    }

    for (int i = start; i <= n; i++) {
        if (!visited[i]) {
            visited[i] = true;
            team_arr[cnt] = i;
            dfs(cnt+1, i);
            visited[i] = false;
        }
    }
}

int main() {
    cin >> n;
    m = n/2;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> s[i][j];
        }
    }

    dfs(0, 1);
    sort(results.begin(), results.end());
    cout << results[0];
}