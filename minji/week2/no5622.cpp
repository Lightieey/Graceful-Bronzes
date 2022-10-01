//
// Created by 김민지 on 2022/09/28.
//
#include "iostream"
#include "string"
using namespace std;

int main() {
    string word;
    cin >> word;

    int sum = 0;
    for(int i = 0; i < word.length(); i++) {
        sum += ((word[i] - 65) / 3) + 3;
        if (word[i] == 'S' || word[i] == 'V' || word[i] == 'Y' || word[i] == 'Z') sum--;
    }

    cout << sum;
    return 0;
}