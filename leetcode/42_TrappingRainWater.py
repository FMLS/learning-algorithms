#class Solution:
#    def trap(self, height):
#        """
#        :type height: List[int]
#        :rtype: int
#        """
#        leftMax = leftMin = 0
#        rightMax = rightMin = 0
#
#        lastLeft = 0
#        lastright = 0
#
#        curLeft = 0
#        curRight = len(height) - 1
#
#        leftTempSum = 0
#        leftTempStep = 0
#        rightTempSum = 0
#        rightTempStep = 0
#
#        leftSum = 0
#        rightSum = 0
#
#        while curLeft <= curRight:
#            if height[curLeft] < leftMax:
#                leftTempSum += leftMax - height[curLeft]
#                leftTempStep += 1
#            if height[curLeft] >= leftMax:
#                leftMax = height[curLeft]
#                leftSum += leftTempSum
#                leftTempSum = 0
#                leftTempStep = 0
#        
#            if height[curRight] < rightMax:
#                rightTempSum += rightMax - height[curRight]
#                rightTempStep += 1
#            if height[curRight] >= rightMax and rightMin < rightMax:
#                rightMax = height[curRight]
#                rightSum += rightTempSum
#                rightTempSum = 0
#                rightTempStep  = 0
#
#
#            lastLeft = height[curLeft]
#            curLeft += 1
#
#            lastright = height[curRight]
#            curRight -= 1
#        
#        if leftTempSum and rightTempSum:
#            if leftMax < rightMax:
#                rightSum += leftTempSum - (rightMax - leftMax) * leftTempStep + rightTempSum
#            if leftMax > rightMax:
#                leftSum += rightTempSum - (leftMax - rightMax) * rightTempStep + leftTempSum
#            else:
#                leftSum += leftTempStep
#                rightSum += rightTempSum
#        
#        return leftSum + rightSum
#
#        #leftMax = hight[curLeft] if hight[curLeft] > leftMax else leftMax
#        #leftMin = hight[curLeft] if 

# 一个非常完美的解法, 思路如下:
# 左右两个指针, 当左边小于等于右边时, 我们把精力放在左边, 因为右边高度已经足够, 不会有右边挡不住水的情况,
# 所以在左侧只要有高度小于当前左侧最高板的, 直接算出容水量(topLeft - height[curLeft]), 如果当前值比
# 已经发现的左侧最大值大, 则更新最大值(这个位置肯定是没水的，因为不是凹陷的)。如果发现右侧值curRight更大,
# 此时从右侧开始注水, 因为这时左侧可以肯定能挡住水, 流程和从左侧一样。
# 当两个指针在中间相遇或者错过

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        curLeft = 0
        curRight = len(height) - 1
        topLeft = 0
        topRight = 0
        sum_ = 0

        while curLeft < curRight:
            if height[curLeft] <= height[curRight]:
                if height[curLeft] < topLeft:
                    sum_ += topLeft - height[curLeft]
                else:
                    topLeft = height[curLeft]
                curLeft += 1
            else:
                if height[curRight] < topRight:
                    sum_ += topRight - height[curRight]
                else:
                    topRight = height[curRight]
                curRight -= 1
        return sum_


if __name__ == '__main__':

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    height = [5, 0, 3, 0, 2]
    res = Solution().trap(height)
    print(res)
