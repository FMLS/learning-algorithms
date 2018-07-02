#include <stdio.h>
#include <stdlib.h>

void merge(int* data, int* tempArr, int lpos, int rpos, int rend, int* count) {
    int i = 0, lend = rpos - 1, tpos = lpos;
    //元素总数
    int totalNum = rend - lpos + 1;
    while(lpos <= lend && rpos <= rend) {
        if (data[lpos] <= data[rpos]) {
            tempArr[tpos++] = data[lpos++];
        } else {
            tempArr[tpos++] = data[rpos++];
        }       
    }

    while(lpos <= lend) {
        tempArr[tpos++] = data[lpos++];
    }
    while(rpos <= rend) {
        tempArr[tpos++] = data[rpos++];
    }

    for(i = 0; i < totalNum; i++, rend--) {
        data[i] = tempArr[i];
//        data[rend] = tempArr[rend];
        count[i]++;
    }
}

void MergeSort(int* data, int left, int right, int *tempArr, int* count) {
    int center = (left + right) / 2;
    if (left < right) {
        MergeSort(data, left, center, tempArr, count);
        MergeSort(data, center + 1, right, tempArr, count);
        merge(data, tempArr, left, center + 1, right, count);
    }
}



int main(void) {
    int i = 0;
    int a[10] = {};
    int tempArr[10] = {};
    for (i = 9; i >= 0; i--) {
        a[i] = i;
        printf("%d ", a[i]);
    }
    printf("\n");
    int center = 10 / 2;
    int count[10] = {};
    MergeSort(a, 0, 9, tempArr, count);
    for (i = 0; i < 10; i++) {
        printf("%d ", a[i]);
    }
    printf("\n");
    for (i = 0; i < 10; i++) {
        printf("%d ", count[i]);
    }
    return 0;
}