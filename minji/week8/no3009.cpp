//
// Created by 김민지 on 2022/11/18.
//
#include "iostream"
#include "vector"
#include "algorithm"
using namespace std;

int main() {
    vector<int> x, y;
    vector<int>::iterator iter;
    for (int i = 0; i < 3; i++) {
        int tx, ty;
        cin >> tx >> ty;

        iter = find(x.begin(), x.end(), tx);
        if (iter != x.end()) {
            x.erase(iter);
        }
        else x.push_back(tx);

        iter = find(y.begin(), y.end(), ty);
        if (iter != y.end()) {
            y.erase(iter);
        }
        else y.push_back(ty);
    }
    cout << x[0] << " " << y[0];
}

//#include <iostream>
//using namespace std;
//
//int main()
//{
//    int x[3];
//    int y[3];
//    for(int i = 0; i < 3; i++)
//        cin >> x[i] >> y[i];
//    if(x[0] == x[1])
//        cout << x[2] << " ";
//    else if(x[0] == x[2])
//        cout << x[1] << " ";
//    else
//        cout << x[0] << " ";
//
//    if(y[0] == y[1])
//        cout << y[2];
//    else if(y[0] == y[2])
//        cout << y[1];
//    else
//        cout << y[0];
//}
