//
// Created by 김민지 on 2022/10/01.
//
#include <iostream>
#include <vector>
#include <sstream>
using namespace std;


int main() {
    string str;
    getline(cin, str);

    vector<string> sptstr;
    istringstream ss(str);
    string temp;

    while (getline(ss, temp, ' ')) {
        sptstr.push_back(temp);
    }

    int count = 0;
    for (string s : sptstr) {
        if (*(s.c_str())) count++;
    }
    cout << count << endl;
}
