//
// Created by 김민지 on 2022/10/27.
//
#include "iostream"
using namespace std;

int COUNT = 0;

void merge(int* nums, int start, int mid, int end, int k) {
    int i = start;
    int j = mid + 1;
    int t = 1;

    int temp[end + 2];
    while (i <= mid && j <= end) {
        if (nums[i] <= nums[j]) {
            temp[t++] = nums[i++];
        } else {
            temp[t++] = nums[j++];
        }
    }

    while (i <= mid) temp[t++] = nums[i++];
    while (j <= end) temp[t++] = nums[j++];
    i = start;
    t = 1;
    while (i <= end) {
        nums[i++] = temp[t++];
        if (++COUNT == k) cout << temp[t-1];
    }
}

void merge_sort(int* nums, int start, int end, int k) {
    if (start < end) {
        int mid = (start + end) / 2;
        merge_sort(nums, start, mid, k);
        merge_sort(nums, mid + 1, end, k);
        merge(nums, start, mid, end, k);
    }
}

int main() {
    int n, k;
    cin >> n >> k;

    int nums[n];
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    merge_sort(nums, 0, n-1, k);
    if (COUNT < k) cout << -1;
}