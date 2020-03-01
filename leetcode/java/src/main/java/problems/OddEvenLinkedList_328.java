package problems;

import tools.ListTool;

/**
 * Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
 *
 * You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
 */

public class OddEvenLinkedList_328 {
    public ListNode oddEvenList(ListNode head) {
        if (head == null || head.next == null || head.next.next == null) return head;

        ListNode headEven = head.next;

        ListNode pCurOdd = head;
        ListNode pCurEven = head.next;

        while (true) {
            pCurOdd.next = pCurEven.next;
            pCurOdd = pCurEven.next;
            if (pCurOdd.next == null) {
                pCurEven.next = null;
                break;
            }

            pCurEven.next = pCurOdd.next;
            pCurEven = pCurOdd.next;
            if (pCurEven.next == null) {
                pCurOdd.next = null;
                break;
            }

        }

        pCurOdd.next = headEven;

        return head;
    }

    public static void main(String[] args) {
        ListNode head = ListTool.createListFromArray(new int[]{1, 2, 3, 4, 5});
        head = ListTool.createListFromArray(new int[] {1});
        head = ListTool.createListFromArray(new int[] {1, 2, 3, 4});
        head = (new OddEvenLinkedList_328()).oddEvenList(head);
        ListTool.printList(head);
    }
}
