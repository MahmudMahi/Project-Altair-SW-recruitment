//merge sort
include <bits/stdc++.h>
using namespace std;
void merge(int array[], int const left, int const mid,
           int const right)
{
    int const subArr1 = mid - left + 1;
    int const subArr2 = right - mid;
    auto *leftArr = new int[subArr1],
         *rightArr = new int[subArr2];
    for (auto i = 0; i < subArr1; i++)
        leftArr[i] = array[left + i];
    for (auto j = 0; j < subArr2; j++)
        rightArr[j] = array[mid + 1 + j];
    auto indOfSubArr1 = 0, indOfSubArr2 = 0;
    int indOfMergedArr = left;
    while (indOfSubArr1 < subArr1
           && indOfSubArr2 < subArr2) {
        if (leftArr[indOfSubArr1]
            <= rightArr[indOfSubArr2]) {
            array[indOfMergedArr]
                = leftArr[indOfSubArr1];
            indOfSubArr1++;
        }
        else {
            array[indOfMergedArr]
                = rightArr[indOfSubArr2];
            indOfSubArr2++;
        }
        indOfMergedArr++;
    }
    while (indOfSubArr1 < subArr1) {
        array[indOfMergedArr]
            = leftArr[indOfSubArr1];
        indOfSubArr1++;
        indOfMergedArr++;
    }
    while (indOfSubArr2 < subArr2) {
        array[indOfMergedArr]
            = rightArr[indOfSubArr2];
        indOfSubArr2++;
        indOfMergedArr++;
    }
    delete[] leftArr;
    delete[] rightArr;
}
void mergeSort(int array[], int const begin, int const end)
{
    if (begin >= end)
        return;

    int mid = begin + (end - begin) / 2;
    mergeSort(array, begin, mid);
    mergeSort(array, mid + 1, end);
    merge(array, begin, mid, end);
}
void printArray(int A[], int size)
{
    for (int i = 0; i < size; i++)
        cout << A[i] << " ";
    cout << endl;
}
int main()
{
    int arr[] = {5, 7, 4, 9, 3, 1, 6, 3, 8};
    int arr_size = sizeof(arr) / sizeof(arr[0]);
    mergeSort(arr, 0, arr_size - 1);
    printArray(arr, arr_size);
    return 0;
}
