package problems;

public class IntersectionOfTwoLinkedLists_160 {
    /**
     * Definition for singly-linked list.
     * public class ListNode {
     *     int val;
     *     ListNode next;
     *     ListNode(int x) {
     *         val = x;
     *         next = null;
     *     }
     * }
     */
    public class Solution {
        public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
            ListNode p1 = headA, p2 = headB;
            int countA = 0, countB = 0;

            while (p1 != null) {
                ++countA;
                p1 = p1.next;
            }

            while (p2 != null) {
                ++countB;
                p2 = p2.next;
            }

            int diff = Math.abs(countA - countB);
            if (countA >= countB) {
                p1 = headA;
                p2 = headB;
            } else {
                p1 = headB;
                p2 = headA;
            }

            for (; diff > 0; --diff) {
                p1 = p1.next;
            }

            while (p1 != null && p2 != null) {
                if (p1 == p2) {
                    return p1;
                }

                p1 = p1.next;
                p2 = p2.next;
            }

            return null;
        }
    }

}
