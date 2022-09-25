//
// Created by 김민지 on 2022/09/23.
//

#include "iostream"
#include "algorithm"
using namespace std;

// 서치함ㅋ
int main(void) {
    // c의 stdio와 cpp의 iostream을 동기화 시켜주는 역할을 하는데,
    // iostream과 stdio의 버퍼를 모두 사용하기 때문에 딜레이가 발생함
    // 따라서, 동기화를 비활성화시켜 실행속도를 빠르게 해줌
    ios_base::sync_with_stdio(0);

    int count = 0;
    int arr[1000001] = {};

    cin >> count;
    for (int i = 0; i < count; i++) {
        cin >> arr[i];
    }

    sort(arr, arr + count);
    cout << arr[0] << " " << arr[count-1];

    return 0;
}