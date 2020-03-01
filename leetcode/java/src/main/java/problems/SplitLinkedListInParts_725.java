package problems;

import tools.ListTool;

public class SplitLinkedListInParts_725 {

    public ListNode[] splitListToParts(ListNode root, int k) {
        int len = this.getLength(root);
        int parts = len / k;
        ListNode[] res = new ListNode[k];
        int index = 0;

        if (parts > 0) {
            int t = len % k;
            for (; index < t; ++index) {
                res[index] = root;
                root = split(root, parts + 1);
            }

            for (; index < k; ++index) {
                res[index] = root;
                root = split(root, parts);
            }
        } else {
            for (; index < len; ++index) {
                res[index] = root;
                root = split(root, 1);
            }

            for (; index < k; ++index) {
                res[index] = null;
            }
        }

        return res;
    }

    public int getLength(ListNode head) {
        int len = 0;
        for (;head != null; head = head.next, ++len);
        return len;
    }

    public ListNode split(ListNode head, int step) {
        for (int i = 1; i < step && head != null; ++i, head = head.next);
        if (head == null) return null;
        ListNode nextHead = head.next;
        head.next = null;
        return nextHead;
    }


    public static void main(String[] args) {
        ListNode head = ListTool.createListFromArray(new int[]{1, 2, 3});
        ListNode[] res = (new SplitLinkedListInParts_725()).splitListToParts(head, 5);
        for (ListNode item : res) {
            System.out.print(item == null ? "null" : item.val + " ");
        }


        head = ListTool.createListFromArray(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 10});
        res = (new SplitLinkedListInParts_725()).splitListToParts(head, 3);
        for (ListNode item : res) {
            System.out.print(item == null ? "null" : item.val + " ");
        }

    }
}
