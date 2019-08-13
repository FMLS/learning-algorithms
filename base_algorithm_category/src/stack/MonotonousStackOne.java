package stack;

import java.util.Stack;

public class MonotonousStackOne {
    public int[][] findLeftRightLatestMin(int[] data) {
        Stack<Integer> stack = new Stack<>();
        int length = data.length;
        int[][] result = new int[length][2];

        for (int p = 0; p < length; ++p) {
            if (stack.empty() || data[p] > data[stack.peek()]) {
                stack.push(p);
            } else {

                while (!stack.empty() && data[p] < data[stack.peek()]) {
                    int item = stack.pop();
                    result[item][0] = stack.empty() ? -1 : stack.peek();
                    result[item][1] = p;
                }

                // 这一步不要漏掉
                stack.push(p);
            }
        }

        // 清算栈中剩余元素
        while (!stack.empty()) {
            int item = stack.pop();
            result[item][0] = stack.empty() ? -1 : stack.peek();
            result[item][1] = -1;
        }

        return result;
    }


    public static void main(String[] args) {
        int[] data = new int[]{3, 4, 1, 5, 6, 2, 7};
        int[][] res = (new MonotonousStackOne()).findLeftRightLatestMin(data);

        for (int[] re : res) {
            System.out.println(re[0] + " " + re[1]);
        }
    }
}
