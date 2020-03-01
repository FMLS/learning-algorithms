package problems;

public class SquaresOfASortedArray {
    public int[] sortedSquares(int[] A) {
        int[] R = new int[A.length];
        int j = 0;
        for (; j < A.length; j++)  {
            if (A[j] >= 0) break;
        }

        int i = j - 1;
        int k = 0;
        while (i >= 0 && j < A.length) {
            if (Math.abs(A[i]) < A[j]) {
                R[k++] = A[i] * A[i];
                i--;
            } else {
                R[k++] = A[j] * A[j];
                j++;
            }
        }

        while (i >= 0) {
            R[k++] = A[i] * A[i];
            i--;
        }
        while (j < A.length) {
            R[k++] = A[j] * A[j];
            j++;
        }

        return R;
    }

    public static void main(String[] args) {
        int[][] tests = new int[][] {
                {0, 1, 2, 3},
                {-3, -2, -1, 0, 1, 2, 3},
                {-7, -3, 2, 3, 11}
        };

        for (int[] test : tests) {

            int[] R = (new SquaresOfASortedArray()).sortedSquares(test);
            for (int i = 0; i < R.length - 1; i++) {
                assert R[i] < R[i + 1];
            }
        }
    }
}
