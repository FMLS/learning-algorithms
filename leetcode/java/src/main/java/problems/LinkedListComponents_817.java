package problems;

import tools.ListTool;

import java.util.HashSet;
import java.util.Set;

/**
 * We are given head, the head node of a linked list containing unique integer values.
 *
 * We are also given the list G, a subset of the values in the linked list.
 *
 * Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.
 */


public class LinkedListComponents_817 {

    public int numComponents(ListNode head, int[] G) {
        Set<Integer> setG = new HashSet<>();
        for (int item : G) {
            setG.add(item);
        }

        int total = 0;
        ListNode p = head;
        while (p != null) {
            if (setG.contains(p.val) && (p.next == null || !setG.contains(p.next.val))) {
                ++total;
            }
            p = p.next;
        }

        return total;
    }

    public static void main(String[] args) {
        ListNode head = ListTool.createListFromArray(new int[]{0, 1, 2, 3, 4});
        int[] G = new int[] { 0, 3, 1, 4};
        int res = (new LinkedListComponents_817()).numComponents(head, G);
        System.out.println(res);
    }
}
