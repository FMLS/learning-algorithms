//
// Created by liuyang on 2019-01-07.
//

#include<vector>
#include<cstdio>

using std::vector;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = 0;
        int sumMax = nums[0];
        for(decltype(nums.size()) i = 0; i < nums.size(); ++i) {
            sum += nums[i];
            sumMax = std::max(sumMax, sum);
            sum = std::max(sum, 0);
        }

        return sumMax;
    }
};


int main(){
    vector<int> data = {-2,1,-3,4,-1,2,1,-5,4};
    Solution s;
    int res = s.maxSubArray(data);
    printf("%d", res);
}