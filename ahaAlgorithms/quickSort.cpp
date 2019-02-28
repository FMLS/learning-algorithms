//
// Created by liuyang on 2019-01-07.
//

#include<vector>
#include<cstdio>

using std::vector;

int partation(vector<int> &nums, int left, int right);

void quickSort(vector<int> &nums, int left, int right) {
    if (left > right) {
        return;
    }

    int mid = partation(nums, left, right);
    quickSort(nums, left, mid - 1);
    quickSort(nums, mid + 1, right);
}

int partation(vector<int> &nums, int left, int right) {

    int target = nums[left];

    int i = left;
    int j = right;

    while(i < j) {
        for (j = right; i < j && nums[j] >= target; --j) {}
        for (i = left; i < j && nums[i] <= target; ++i) {}
        if (i < j) {
            std::swap(nums[i], nums[j]);
        }
    }
    std::swap(nums[left], nums[i]);
    return i;
}

int main() {
    vector<int> data = {6, 1, 2, 7, 9, 3, 4, 5, 10, 8};
    quickSort(data, 0, int(data.size() - 1));
    for(auto i : data) {
        printf("%d ", i);
    }
}
