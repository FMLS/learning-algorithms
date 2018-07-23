import heapq

class Solution:
    
    # AC 24% 
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        data = []
        for elem in nums:
            if len(data) < k:
                heapq.heappush(data, elem)
            elif elem > data[0]:
                data[0] = elem
                heapq.heapify(data)

        return data[0]

if __name__ == '__main__':
    data = [3, 2, 1, 5, 6, 4]
    data = [3,2,3,1,2,4,5,5,6]
    ans = Solution().findKthLargest(data, 4)
    print(data)
    print(ans)
