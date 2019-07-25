package problems;


import tools.ListTool;

public class ReverseLinkedList_206 {

     public static ListNode reverseList(ListNode head) {

          ListNode p1 = null;
          ListNode p2 = head;
          ListNode p3;

          while (p2 != null) {
               p3 = p2.next;
               p2.next = p1;
               p1 = p2;
               p2 = p3;
          }

          return p1;
     }

     public static void main(String[] args) {
         ListNode a = ListTool.createListFromArray(new int[]{1, 2, 3, 4});
         ListNode p = reverseList(a);
         ListTool.printList(p);

         a = ListTool.createListFromArray(new int[]{1, 2});
         p = reverseList(a);
         ListTool.printList(p);

         a = ListTool.createListFromArray(new int[]{1});
         p = reverseList(a);
         ListTool.printList(p);
     }
}
