//
// Created by 김민지 on 2022/09/23.
//

#include <iostream>
using namespace std;

int main(void) {

    int king, queen, look, bishop, night, phon;
    cin >> king >> queen >> look >> bishop >> night >> phon;

    king = 1 - king;
    queen = 1 - queen;
    look = 2 - look;
    bishop = 2 - bishop;
    night = 2 - night;
    phon = 8 - phon;

    cout << king << " " << queen << " " << look << " " << bishop << " " << night << " " << phon << endl;

}
