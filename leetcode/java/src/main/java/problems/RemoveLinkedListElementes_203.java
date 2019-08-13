package problems;

import tools.ListTool;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

public class RemoveLinkedListElementes_203 {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode prev = dummy;
        ListNode p = dummy.next;

        while (p != null) {
            if (p.val == val) {
                prev.next = p.next;
            } else {
                prev = prev.next;
            }
            p = p.next;
        }

        return dummy.next;
    }

    public static void main(String[] args) {
        ListNode head = ListTool.createListFromArray(new int[]{1, 2, 6, 6, 6, 3, 4, 5, 6});
        head = (new RemoveLinkedListElementes_203().removeElements(head, 6));
        ListTool.printList(head);

        head = ListTool.createListFromArray(new int[]{1, 1, 1});
        head = (new RemoveLinkedListElementes_203().removeElements(head, 1));
        ListTool.printList(head);

    }
}
