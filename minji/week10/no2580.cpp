//
// Created by 김민지 on 2022/12/03.
//
#include "iostream"
#include "vector"
using namespace std;

int problem[9][9] = {0,};
vector<pair<int, int>> points;
bool found = false;
int n;

bool check_vertical(int i, int k) {
    for (int j = 0; j < 9; j++) {
        if (problem[i][j] - k == 0) return 0;
    }
    return 1;
}

bool check_horizontal(int j, int k) {
    for (int i = 0; i < 9; i++) {
        if (problem[i][j] - k == 0) return 0;
    }
    return 1;
}

bool check_square(int i, int j, int k) {
    for (int x = (i/3)*3; x < (i/3)*3+3; x++) {
        for (int y = (j/3)*3; y < (j/3)*3+3; y++) {
            if (problem[x][y] - k == 0) return 0;
        }
    }
    return 1;
}


void sudoku(int cnt) {
    if (cnt == n) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                cout << problem[i][j] << " ";
            }
            cout << "\n";
        }
        found = true;
        return;
    }

    int i = points[cnt].first;
    int j = points[cnt].second;
    for (int k = 1; k < 10; k++) {
        bool c1 = check_vertical(i, k);
        bool c2 = check_horizontal(j, k);
        bool c3 = check_square(i, j, k);
        if (c1 & c2 & c3) {
            problem[i][j] = k;
            sudoku(cnt+1);
        }
        if (found) return;
    }
    problem[i][j] = 0;
}

int main() {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cin >> problem[i][j];
            if (problem[i][j] == 0) {
                n++;
                points.push_back(pair<int, int>(i, j));
            }
        }
    }
    sudoku(0);
}