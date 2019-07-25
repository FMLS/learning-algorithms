package problems;

import tools.ListTool;

/**
 *
 Given a linked list, remove the n-th node from the end of list and return its head.

 Example:

 Given linked list: 1->2->3->4->5, and n = 2.

 After removing the second node from the end, the linked list becomes 1->2->3->5.
 Note:

 Given n will always be valid.

 Follow up:

 Could you do this in one pass?
 */
public class RemoveNthNodeFromEndOfList_19 {

    // Two pass algorithm
    //public ListNode removeNthFromEnd(ListNode head, int n) {
    //    ListNode dummy = new ListNode(0);
    //    dummy.next = head;

    //    int length = 0;
    //    ListNode p = head;
    //    while(p != null) {
    //        length++;
    //        p = p.next;
    //    }

    //    p = dummy;
    //    length -= n;
    //    while(length > 0) {
    //        p = p.next;
    //        length--;
    //    }

    //    p.next = p.next.next;
    //    return dummy.next;
    //}


    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode first = dummy;
        ListNode second = dummy;

        for (int i = 0; i < n + 1 && first != null; i++) {
            first = first.next;
        }

        while (first != null) {
            first = first.next;
            second = second.next;
        }

        second.next = second.next.next;
        return dummy.next;
    }

    public static void main(String[] args) {
        ListNode l1 = ListTool.createListFromArray(new int[]{1, 2, 3, 4, 5});
        l1 = (new RemoveNthNodeFromEndOfList_19()).removeNthFromEnd(l1, 2);
        ListTool.printList(l1);
    }
}
