//
// Created by 김민지 on 2022/09/30.
//
#include "iostream"
#include "string"
#include "vector"
#include "algorithm"
using namespace std;

int main() {
    int n, count;
    cin >> n;
    count = n;

    for(int i = 0; i < n; i++) {
        string str;
        vector<char> v;
        cin >> str;

        for (int j = 0; j < str.length(); j++) {
            v.push_back(str[j]);
        }
        sort(v.begin(), v.end());
        v.erase(unique(v.begin(), v.end()), v.end());

        for(int j = 0; j < v.size(); j++) {
            size_t pos1 = str.find(v[j]), pos2;
            bool flag = true;
            while (pos1 != str.length() - 1) {
                pos2 = str.find_first_of(v[j], pos1 + 1);
                if (pos2 == string::npos) break;
                if (pos2 - pos1 > 1) {
                    flag = false;
                    break;
                }
                pos1 = pos2;
            }
            if (flag == false) {
                count--;
                break;
            }
        }
    }

    cout << count;
}

/* 잘 푼 사람 코드... ... 나 너무 멍청..
int main(){
	int n;
	int cnt = 0;
	string str;
	cin >> n;

	for(int i=0; i<n; i++){
		cin >> str;
		int size = str.length();
		bool flag = true;

		for(int j=0; j<size; j++){
			for(int k=0; k<j; k++){
				if(str[j] != str[j-1] && str[j] == str[k]){
					flag = false;
					break;
				}
			}
		}
		if(flag) cnt++;
	}

	cout << cnt;

    return 0;
}
 */