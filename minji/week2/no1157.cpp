//
// Created by 김민지 on 2022/09/26.
//
#include "iostream"
#include "string"
using namespace std;

int main() {
    string word;
    cin >> word;

    int alphabet[26] = {};
    for (int i = 0; i < word.length(); i++) {
        word[i] = toupper(word[i]);
        alphabet[word[i]-65]++;
    }

    int maxidx = 0;
    for (int i = 0; i < 26; i++) {
        if (alphabet[i] > alphabet[maxidx]) maxidx = i;
    }

    for (int i = 0; i < 26; i++) {
        if (i != maxidx && alphabet[i] == alphabet[maxidx]) {
            cout << "?";
            return 0;
        }
    }
    cout << (char)(maxidx + 65);
    return 0;
}