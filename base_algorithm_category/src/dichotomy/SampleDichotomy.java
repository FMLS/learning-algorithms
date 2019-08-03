package dichotomy;
/**
 * 简单二分查找
 */
public class SampleDichotomy {

    public static int findByDichotomy(int[] data, int key) {
        int lo = 0;
        int hi = data.length - 1;
        int mid;

        while (lo <= hi) {
            mid = lo + (hi - lo) / 2;
            if (data[mid] == key) {
                return mid;
            } else if (data[mid] < key) {
                lo = mid + 1;
            } else if (data[mid] > key) {
                hi = mid - 1;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] data = new int[10];
        for (int i = 0 ;i < 10; i++) {
            data[i] = i;
        }

        int res = findByDichotomy(data, 11);
        System.out.println(res);
    }


}
