package problems;

public class LinkedListCycle_141 {
   // public boolean hasCycle(ListNode head) {
   //     if (head == null) {
   //         return false;
   //     }

   //     ListNode slow, fast;
   //     slow = fast = head;

   //     while (fast.next != null && fast.next.next != null) {
   //         slow = slow.next;
   //         fast = fast.next.next;

   //         if (slow == fast) {
   //             return true;
   //         }
   //     }

   //     return false;
   //}

    public boolean hasCycle(ListNode head) {
        if (head == null) {
            return false;
        }

        ListNode slow, fast;
        slow = fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast) {
                return true;
            }
        }

        return false;
   }
}
