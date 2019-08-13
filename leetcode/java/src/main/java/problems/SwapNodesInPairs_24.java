package problems;

import tools.ListTool;

import javax.tools.Tool;
import java.util.List;

public class SwapNodesInPairs_24 {
    public ListNode swapPairs(ListNode head) {

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode cur = dummy;

        while (cur.next != null && cur.next.next != null) {
            ListNode first = cur.next;
            ListNode second = cur.next.next;

            cur.next = second;
            first.next = second.next;
            second.next = first;
            // 注意这一步, cur要指向交换节点的前一个节点, 这也是我们用dummy节点的原因
            cur = first;
        }

        return dummy.next;
    }

    public static void main(String[] args) {
        ListNode head = ListTool.createListFromArray(new int[]{1, 2, 3, 4});
        head = (new SwapNodesInPairs_24()).swapPairs(head);
        ListTool.printList(head);

    }
}
