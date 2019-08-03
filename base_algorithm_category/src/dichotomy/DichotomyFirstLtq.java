package dichotomy;
/**
 * 二分法找重复元素数组中第一个小于等于给定值的位置
 */
public class DichotomyFirstLtq {
    public static int findByDichotomy(int[]data, int key) {
        int lo, hi, mid;
        lo = 0;
        hi = data.length - 1;

        while (lo <= hi) {
            mid = lo + (hi - lo) / 2;
            if (data[mid] <= key) {
                if (mid == data.length - 1 || data[mid + 1] > key) {
                    return mid;
                }
                lo = mid + 1;

            }
            else {
                hi = mid - 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] data = new int[]{1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 8};

        for (int i: data) {
            System.out.printf("%2d ", i);
        }
        System.out.println();
        for (int i = 0; i < data.length; i++) {
            System.out.printf("%2d ", i);
        }
        System.out.println();

        int index = findByDichotomy(data, 6);
        System.out.println(index);
    }

}
