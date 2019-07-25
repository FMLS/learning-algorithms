package problems;

import tools.ListTool;

public class RemoveDuplicatesFromSortedList_83 {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode p, q;
        p = q = head;

        while (p != null) {
            while (q != null && p.val == q.val) {
                q = q.next;
            }

            p.next = q;
            p = q;
        }

        return head;
    }

    public static void main(String[] args) {
        ListNode l = ListTool.createListFromArray(new int[]{1, 1, 2, 3, 3});
        l = (new RemoveDuplicatesFromSortedList_83()).deleteDuplicates(l);
        ListTool.printList(l);

        l = ListTool.createListFromArray(new int[]{1, 1});
        l = (new RemoveDuplicatesFromSortedList_83()).deleteDuplicates(l);
        ListTool.printList(l);
    }
}
