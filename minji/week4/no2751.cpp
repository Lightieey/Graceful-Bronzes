//
// Created by 김민지 on 2022/10/13.
//
#include "iostream"
using namespace std;

void merge(int* arr, int* tempArr, int begin, int mid, int end) {
    int i = begin;
    int j = mid + 1;
    int sortIdx = begin;

    while (i <= mid && j <= end) {
        if (arr[i] <= arr[j])
            tempArr[sortIdx++] = arr[i++];
        else
            tempArr[sortIdx++] = arr[j++];
    }

    // 왼쪽이 오른쪽보다 모두 작은 경우
    if (i > mid) {
        while (j <= end) tempArr[sortIdx++] = arr[j++];
    }
    // 오른쪽이 왼쪽보다 모두 작은 경우
    if (j > end) {
        while (i <= mid) tempArr[sortIdx++] = arr[i++];
    }

    for (int k = begin; k <= end; k++) arr[k]= tempArr[k];
}

void mergeSort(int* arr, int* res, int begin, int end) {
    int mid;
    if (begin < end) {
        mid = (begin + end) / 2;
        mergeSort(arr, res, begin, mid);
        mergeSort(arr, res, mid + 1, end);
        merge(arr, res, begin, mid, end);
    }
}

int main() {
    int n;
    cin >> n;
    int nums[n];

    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    int temp[n];
    mergeSort(nums, temp, 0, n-1);

    for (int i = 0; i < n; i++) {
        cout << nums[i] << "\n";
    }

    return 0;
}