package problems;
import tools.ListTool;

/*
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
*/
public class AddTwoNumbers_2 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        int carry = 0;
        int sum = 0;
        ListNode p1 = l1;
        ListNode p2 = l2;

        while (p1.next != null && p2.next != null) {
            sum = p1.val + p2.val + carry;
            p1.val = sum % 10;
            carry = sum / 10;
            p1 = p1.next;
            p2 = p2.next;
        }

        if (p1.next == null && p2.next == null) {
            sum = p1.val + p2.val + carry;
            p1.val = sum % 10;
            carry = sum / 10;
            if (carry != 0) {
                p1.next = new ListNode(carry);
            }
            return l1;
        }

        if (p1.next == null) {
            sum = p1.val + p2.val + carry;
            p1.val = sum % 10;
            carry = sum / 10;
            p1.next = p2.next;
            p1 = p1.next;

            while (p1.next != null) {
                sum = p1.val + carry;
                p1.val = sum % 10;
                carry = sum / 10;
                p1 = p1.next;
            }
        }

        if (p2.next == null) {
            sum = p1.val + p2.val + carry;
            p1.val = sum % 10;
            carry = sum / 10;
            p1 = p1.next;

            while (p1.next != null) {
                sum = p1.val + carry;
                p1.val = sum % 10;
                carry = sum / 10;
                p1 = p1.next;
            }

        }

        sum = p1.val + carry;
        p1.val = sum % 10;
        carry = sum / 10;

        if (carry != 0) {
            p1.next = new ListNode(carry);
        }

        return l1;
    }

    public static void main(String[] args) {
        ListNode l1 = ListTool.createListFromArray(new int[]{2, 4 ,3});
        ListNode l2 = ListTool.createListFromArray(new int[]{5, 6, 4});
        ListNode head = (new AddTwoNumbers_2()).addTwoNumbers(l1, l2);
        ListTool.printList(head);


        l1 = ListTool.createListFromArray(new int[]{5});
        l2 = ListTool.createListFromArray(new int[]{5});
        head = (new AddTwoNumbers_2()).addTwoNumbers(l1, l2);
        ListTool.printList(head);


        l1 = ListTool.createListFromArray(new int[]{5});
        l2 = ListTool.createListFromArray(new int[]{0});
        head = (new AddTwoNumbers_2()).addTwoNumbers(l1, l2);
        ListTool.printList(head);


        l1 = ListTool.createListFromArray(new int[]{9, 9, 9});
        l2 = ListTool.createListFromArray(new int[]{1});
        head = (new AddTwoNumbers_2()).addTwoNumbers(l1, l2);
        ListTool.printList(head);


        l1 = ListTool.createListFromArray(new int[]{9, 9, 9});
        l2 = ListTool.createListFromArray(new int[]{9, 9, 9});
        head = (new AddTwoNumbers_2()).addTwoNumbers(l1, l2);
        ListTool.printList(head);
    }
}
