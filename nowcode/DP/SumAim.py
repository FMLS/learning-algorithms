# 给定一个数组arr 和 一个整数aim, 如果可以任意选择arr中的数字,
# 能不能累加得到aim, 返回True 或 False
# 数组arr中和aim都为非负整数
class Solution:
    def sumAim(self, arr, aim, i, sum_):
        if i == len(arr):
            return sum_ == aim

        choice1 = self.sumAim(arr, aim, i + 1, sum_ + arr[i])
        choice2 = self.sumAim(arr, aim, i + 1, sum_)
        return choice1 or choice2
    
    def dpSumAim(self, arr, aim):
        pass

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
