package problems;

/**
 * Implement int sqrt(int x).
 *
 * Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
 *
 * Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
 */

public class SqrtX_69 {
    // 第一次写的溢出答案
    //public int mySqrt(int x) {
    //    int lo = 0;
    //    int hi = x;

    //    while (lo <= hi) {
    //        int mid = lo + (hi - lo) / 2;
    //        int res = mid * mid;

    //        if (res > x) {
    //            hi = mid - 1;
    //        }else if (res < x) {
    //            lo = mid + 1;
    //        } else {
    //            return mid;
    //        }
    //    }
    //    return hi;
    //}

    /**
     * 尝试另一个
     */

    public int mySqrt2(int x) {
        // 防止除零
        if (x == 0) return 0;

        // lo从1开始, 防止除零
        int lo = 1;
        int hi = x;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            // 使用x/mid避免溢出
            if (mid == x / mid) {
                return mid;
            } else if (mid < x / mid) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        return hi;
    }


    /**
     *leetcode上一个比较优秀的答案, 巧妙避免溢出
     *https://leetcode.com/problems/sqrtx/discuss/25198/3-JAVA-solutions-with-explanation
     *
     */
    public int mySqrt(int x) {
        if (x == 0) return 0;
        int start = 0, end = x;
        while (start < end) {
            int mid = start + (end - start) / 2;
            if (mid <= x / mid && (mid + 1) > x / (mid + 1)) {
                return mid;
            } else if (mid > x / mid) {
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        return start;
    }

    public static void main(String[] args) {
        int x = (new SqrtX_69()).mySqrt2(1);
        System.out.println(x);
    }
}
