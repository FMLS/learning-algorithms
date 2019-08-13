package problems;

import java.util.Stack;

public class MinStack_155 {

    private Stack<Integer> stack;
    private int min;

    /** initialize your data structure here. */
    public MinStack_155() {
        stack = new Stack<>();
        min = Integer.MAX_VALUE;
    }

    public void push(int x) {
        /**
         * 这个<=判断而不是<
         * 应对下面这个case
         * ["MinStack","push","push","push","getMin","pop","getMin"]
         * [[],[0],[1],[0],[],[],[]]
         */
        if (x <= min) {
            stack.push(min);
            min = x;
        }

        stack.push(x);
    }

    public void pop() {
        int res = stack.pop();
        if (res == min) {
            min = stack.pop();
        }
    }

    public int top() {
        return stack.peek();
    }

    public int getMin() {
        return min;
    }

    public static void main(String[] args) {
        int min, top;

        MinStack_155 minStack_155 = new MinStack_155();
        minStack_155.push(-2);
        minStack_155.push(0);
        minStack_155.push(-3);
        min = minStack_155.getMin();
        System.out.println(min);
        minStack_155.pop();
        top = minStack_155.top();
        System.out.println(top);
        min = minStack_155.getMin();
        System.out.println(min);
    }
}
