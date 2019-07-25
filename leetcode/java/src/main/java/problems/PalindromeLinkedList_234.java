package problems;

import tools.ListTool;

import java.util.Stack;

public class PalindromeLinkedList_234 {

    public boolean isPalindrome(ListNode head) {
        ListNode slow, fast;
        slow = fast = head;
        Stack<ListNode> stack = new Stack<>();

        while(fast != null && fast.next != null) {
            stack.push(slow);
            slow = slow.next;
            fast = fast.next.next;
        }


        if (fast != null && fast.next == null) {
            slow = slow.next;
        }

        while (!stack.empty()) {
            if (stack.pop().val != slow.val) {
                return false;
            }
            slow = slow.next;
        }

        return true;
    }

    public static void main(String[] args) {
        ListNode l = ListTool.createListFromArray(new int[]{1, 2});
        boolean res = (new PalindromeLinkedList_234()).isPalindrome(l);
        System.out.println(res);
    }
}
