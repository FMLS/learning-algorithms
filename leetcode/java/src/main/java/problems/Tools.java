package problems;

import java.util.ArrayList;
import java.util.List;

public class Tools {
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
        List<String> datas = new ArrayList<>();
        while (head != null) {
            datas.add(String.valueOf(head.val));
            head = head.next;
        }
        String res = String.join(",", datas);
        System.out.println(res);
    }
}
