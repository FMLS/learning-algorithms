package problems;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class SpiralMatrix_54 {
    public List<Integer> spiralOrder(int[][] matrix) {
        if (matrix.length == 0) return new ArrayList<>();

        int tR = 0, tC = 0;
        int dR = matrix.length - 1;
        int dC = matrix[0].length - 1;

        List<Integer> result = new ArrayList<>((dR + 1) * (dC + 1));

        while (tR <= dR && tC <= dC) {
            this.addItem(matrix, tR++, tC++, dR--, dC--, result);
        }

        return result;
    }

    private void addItem(int[][]m, int tR, int tC, int dR, int dC, List<Integer> result) {
        //只有一行
        if (tR == dR) {
            while (tC <= dC) result.add(m[tR][tC++]);
        } else if (tC == dC) {
            while (tR <= dR) result.add(m[tR++][tC]);
        } else {
            int curR = tR;
            int curC = tC;
            while (curC != dC) result.add(m[curR][curC++]);
            while (curR != dR) result.add(m[curR++][curC]);
            while (curC != tR) result.add(m[curR][curC--]);
            while (curR != tR) result.add(m[curR--][curC]);
        }
    }

    public static void main(String[] args) {
        //int counter = 0;
        //int[][] matrix = new int[4][4];
        //for (int i = 0; i < matrix.length; i++) {
        //    for (int j = 0; j < matrix[0].length; j++) {
        //        matrix[i][j] = ++counter;
        //    }
        //}

        //int[][] matrix = {
        //    {1, 2, 3},
        //    {4, 5, 6},
        //    {7, 8, 9}
        //};

        int[][] matrix = new int[3][0];

        List res = (new SpiralMatrix_54()).spiralOrder(matrix);
        res.forEach(System.out::println);
    }
}
