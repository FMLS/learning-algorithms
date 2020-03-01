package problems;

import java.util.Arrays;

public class SpiralMatrix2_59 {
    public int[][] generateMatrix(int n) {
        int counter = 1;
        int[][] matrix = new int[n][n];

        int tR = 0, tC = 0, dR = n - 1, dC = n - 1;

        for (; tR <= dR && tC <= dC; tR++, tC++, dR--, dC--) {
            if (tR == dR) while (tC <= dC) matrix[tR][tC++] = counter++;
            else if (tC == dC) while (tR <= dR) matrix[tR++][tC] = counter++;
            else {
                int curR = tR, curC = tC;

                while (curC != dC) matrix[curR][curC++] = counter++;
                while (curR != dR) matrix[curR++][curC] = counter++;
                while (curC != tC) matrix[curR][curC--] = counter++;
                while (curR != tR) matrix[curR--][curC] = counter++;
            }
        }

        return matrix;
    }

    public static void main(String[] args) {
        int[][] matrix = (new SpiralMatrix2_59().generateMatrix(0));

        for (int[] row : matrix) {
            for (int item : row) {
                System.out.printf("%2d ", item);
            }
            System.out.println();
        }

    }
}
