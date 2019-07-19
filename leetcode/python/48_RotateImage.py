class Solution:

    # clockwise rotate
    # first reverse up to down, then swap the symmetry 
    # 1 2 3     7 8 9     7 4 1
    # 4 5 6  => 4 5 6  => 8 5 2
    # 7 8 9     1 2 3     9 6 3

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(0, len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    
    # anticlockwise rotate
    # first reverse left to right, then swap the symmetry
    # 1 2 3     3 2 1     3 6 9
    # 4 5 6  => 6 5 4  => 2 5 8
    # 7 8 9     9 8 7     1 4 7

    def anti_rotate(self, matrix):
        for ls in matrix:
            ls.reverse()
        for i in range(0, len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    data = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    #data = [
    #    [ 5, 1, 9,11],
    #    [ 2, 4, 8,10],
    #    [13, 3, 6, 7],
    #    [15,14,12,16]
    #]
    #Solution().rotate(data)
    Solution().anti_rotate(data)
    print(data)
