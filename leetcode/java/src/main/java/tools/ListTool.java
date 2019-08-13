package tools;

import problems.ListNode;

import java.util.ArrayList;
import java.util.List;

public class ListTool {
    public static ListNode createListFromArray(int[] nodes) {
        if (nodes.length == 0) {
            return null;
        }

        ListNode head = new ListNode(nodes[0]);
        ListNode p = head;

        for (int i = 1; i < nodes.length; ++i) {
            p.next = new ListNode(nodes[i]);
            p = p.next;
        }

        return head;
    }

    public static void printList(ListNode head) {
        if (head == null) System.out.println("null");
        List<String> datas = new ArrayList<>();
        while (head != null) {
            datas.add(String.valueOf(head.val));
            head = head.next;
        }
        String res = String.join(",", datas);
        System.out.println(res);
    }

    public static ListNode getLastNode(ListNode head) {
        if (head == null) return null;
        while (head.next != null) {
            head = head.next;
        }
        return head;
    }

    public static int getLength(ListNode head) {
        if (head == null) return 0;
        int count = 0;
        while (head != null) {
            ++count;
            head = head.next;
        }

        return count;
    }

    public static ListNode getNodeByIndex(ListNode head, int index) {
        while (head != null) {
            if (--index == 0) return head;
            head = head.next;
        }

        return null;
    }
}
