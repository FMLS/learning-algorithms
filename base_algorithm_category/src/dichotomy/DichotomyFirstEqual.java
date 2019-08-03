package dichotomy;
import java.text.MessageFormat;

/**
 * 二分法找重复元素数组中第一个等于key的位置
 */
public class DichotomyFirstEqual {
    public static int findByDichotomy(int[] data, int key) {
        int lo = 0;
        int hi = data.length - 1;
        int mid;

        while (lo < hi) {
            mid = lo + (hi - lo) / 2;
            if (key <= data[mid]) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }

        if (data[lo] == key) {
            return lo;
        }

        return -1;
    }

    public static int findByDichotomyGeekTime(int[] data, int key) {
        int lo = 0;
        int hi = data.length - 1;
        int mid;

        while (lo <= hi) {
            mid = lo + (hi - lo) / 2;
            if (key < data[mid]) {
                hi = mid - 1;
            } else if (key > data[mid]){
                lo = mid + 1;
            } else {
                if ((mid == 0) || data[mid - 1] != key) {
                    return mid;
                }
                hi = mid - 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] data = new int[]{1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 8};

        for (int i = 1; i <= 8; i++) {
            int res1 = findByDichotomy(data, i);
            int res2 = findByDichotomyGeekTime(data, i);
            System.out.println(MessageFormat.format("{0} -> {1} - {2}", i, res1, res2));
            assert res1 == res2;
        }
    }

}
