package dichotomy;
/**
 * 二分法找重复元素数组中最后一个等于给定值的位置
 */
public class DichotomyLastEqual {
    public static int findByDichotomyGeekTime(int[] data, int key) {
        int lo, hi, mid;
        lo = 0;
        hi = data.length - 1;

        while (lo <= hi) {
            mid = lo + (hi - lo) / 2;
            if (key < data[mid]) {
                hi = mid - 1;
            } else if (key > data[mid]) {
                lo = mid + 1;
            } else {
                if (mid == data.length - 1 || (data[mid + 1] != key)) {
                    return mid;
                }
                lo = mid + 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] data = new int[]{1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 8, 8, 8};

        for (int i: data) {
            System.out.printf("%2d ", i);
        }
        System.out.println();
        for (int i = 0; i < data.length; i++) {
            System.out.printf("%2d ", i);
        }
        System.out.println();

        int res1 = findByDichotomyGeekTime(data, 8);
        System.out.println(res1);
    }

}
