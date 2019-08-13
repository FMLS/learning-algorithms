package problems;

import tools.ListTool;

import java.util.Stack;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

public class NextGreaterNodeInLinkedList_1019 {

    // 暴力解法
    public int[] nextLargerNodes(ListNode head) {

        if (head == null) return new int[0];
        int length = this.getListLength(head);
        int[] res = new int[length];
        int count = 0;
        for (ListNode p = head; p != null; p = p.next) {
            ListNode q = p.next;
            // 这个判断条件是<=, 因为只有大于或者到末尾才停, 这点容易出错
            for (; q != null && q.val <= p.val; q = q.next);
            if (q == null) {
                res[count] = 0;
            } else {
                res[count] = q.val;
            }
            ++count;
        }
        return res;
    }

    // 单调栈解法
    public int[] nextLargerNodes2(ListNode head) {
        if (head == null) return new int[0];

        int length = this.getListLength(head);
        int[] res = new int[length];
        int count = 0;
        Stack<Integer> stack = new Stack<>();

        for (ListNode p = head; p != null; p = p.next) {
            // 这里我们需要用"值"比大小, 所以底层需要放"值", 第二层是其在数组中的位置
            if (stack.empty() || p.val < stack.peek()) {
                stack.push(count);
                stack.push(p.val);
            } else {
                while (!stack.empty() && p.val > stack.peek()) {
                    stack.pop();
                    int index = stack.pop();
                    res[index] = p.val;
                }
                stack.push(count);
                stack.push(p.val);
            }
            ++count;
        }

        while (!stack.empty()) {
            stack.pop();
            int index = stack.pop();
            res[index] = 0;
        }

        return res;
    }

    private int getListLength(ListNode head) {
        int total = 0;
        for (ListNode p = head; p != null; p = p.next, ++total);
        return total;
    }


    public static void main(String[] args) {
        int[] array = new int[] {1, 7, 5, 1, 9, 2, 5, 1};

        ListNode head = ListTool.createListFromArray(array);
        int[] res = (new NextGreaterNodeInLinkedList_1019()).nextLargerNodes(head);
        for (int re : res) {
            System.out.print(re + " ");
        }

        System.out.println();

        int[] res2 = (new NextGreaterNodeInLinkedList_1019()).nextLargerNodes2(head);
        for (int re : res2) {
            System.out.print(re + " ");
        }
    }
}
