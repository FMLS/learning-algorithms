package problems;

import tools.ListTool;

public class MergeTwoSortedList_21 {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

        if (l1 == null) return l2;
        if (l2 == null) return l1;

        ListNode head, cur;
        if (l1.val <= l2.val) {
            cur = head = l1;
            l1 = l1.next;
        } else {
            cur = head = l2;
            l2 = l2.next;
        }


        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                cur.next = l1;
                l1 = l1.next;
            } else {
                cur.next = l2;
                l2 = l2.next;
            }
            cur = cur.next;
        }

        if (l1 != null) {
            cur.next = l1;
        } else {
            cur.next = l2;
        }

        return head;
    }

    public static void main(String[] args) {
        ListNode l1 = ListTool.createListFromArray(new int[]{1, 2, 4});
        ListNode l2 = ListTool.createListFromArray(new int[]{1, 3, 4});

        ListNode newlist = (new MergeTwoSortedList_21()).mergeTwoLists(l1, l2);
        ListTool.printList(newlist);


        l1 = ListTool.createListFromArray(new int[]{5});
        l2 = ListTool.createListFromArray(new int[]{1, 2, 4});

        newlist = (new MergeTwoSortedList_21()).mergeTwoLists(l1, l2);
        ListTool.printList(newlist);
    }
}
