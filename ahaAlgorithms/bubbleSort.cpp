//
// Created by liuyang on 2019-01-07.
//

#include<cstdio>
#include<vector>

using std::vector;

void bubbleSort(vector<int> &nums) {
    for (decltype(nums.size()) i = 0; i < nums.size(); ++i) {
        for (decltype(nums.size()) j = 0; j < nums.size() - 1 - i; ++j) {
            if (nums[j] > nums[j + 1]) {
                std::swap(nums[j], nums[j + 1]);
            }
        }
    }
}

int main() {
    vector<int> data = {9, 7, 4, 6, 3, 5, 1, 2, 8, -1};
    printf("before sort:");
    for (const auto &item : data) {
        printf("%d ", item);
    }
    bubbleSort(data);

    printf("after sorted:");
    for (const auto &item : data) {
        printf("%d ", item);
    }
}