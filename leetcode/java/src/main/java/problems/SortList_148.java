package problems;

import tools.ListTool;

import java.util.List;

public class SortList_148 {
    /**
     * Definition for singly-linked list.
     * public class ListNode {
     *     int val;
     *     ListNode next;
     *     ListNode(int x) { val = x; }
     * }
     */


    // 标准答案, 自顶向下递归处理
    // leetcode 最高votes
    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        // step 1. cut the list to two halves
        // fast != null && fast.next != null 这种判断条件下, 如果中间节点是向下取整, 则slow是中间节点的下一个节点
        // prev 记录链表的是中间节点
        ListNode prev = null, slow = head, fast = head;

        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }

        // 断开链表, 物理上一分为二
        prev.next = null;

        //step 2. sort each half
        ListNode l1 = sortList(head);
        ListNode l2 = sortList(slow);

        // step 3. merge l1, l2;
        return merge(l1, l2);
    }

    // 此方法是常规的merge list操作, 返回新的头结点
    private ListNode merge(ListNode l1, ListNode l2) {
        // dummy node
        ListNode l = new ListNode(0), p = l;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                p.next = l1;
                l1 = l1.next;
            } else {
                p.next = l2;
                l2 = l2.next;
            }

            p = p.next;
        }

        if (l1 != null) {
            p.next = l1;
        }

        if (l2 != null) {
            p.next = l2;
        }

        return l.next;
    }

//---------------------------------------------------------------------------------------------------------//

    // 标准答案, 自底向上迭代处理
    public void sortListBU(ListNode head) {
        int N = ListTool.getLength(head);
        for (int sz = 1; sz < N; sz = sz + sz) {
            for (int lo = 0; lo < N - sz; lo += sz + sz) {

            }
        }
    }

    public static ListNode mergeList(ListNode lo, ListNode mid, ListNode hi) {
        ListNode dummy = new ListNode(0);
        ListNode p = lo, q = mid.next;
        ListNode cur = dummy;
        while (p != mid.next && q != hi.next) {
            if (p.val > q.val) {
                cur.next = q;
                q = q.next;
            } else {
                cur.next = p;
                p = p.next;
            }

            cur = cur.next;
        }

        if (p != mid.next) {
            cur.next = p;
        }

        if (q != hi.next) {
            cur.next = q;
        }

        return dummy.next;
    }

    public static ListNode getMidNode(ListNode lo, ListNode hi) {
        ListNode slow = lo, fast = lo;
        while (fast.next != hi && fast != hi) {
            slow = slow.next;
            fast = fast.next.next;
        }

        return slow;
    }


    public ListNode mySortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        // step 1. cut the list to two halves
        ListNode prev = null, slow = head, fast = head;

        while (fast.next != null && fast.next.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }

        // 断开链表, 物理上一分为二
        // prev.next = null;
        ListNode head2 = slow.next;
        slow.next = null;

        // step 2. sort each half
        // 这一步要用新的头结点
        ListNode l1 = sortList(head);
        ListNode l2 = sortList(head2);

        // step 3. merge l1, l2;
        // 返回merge过后新的头结点
        return merge(l1, l2);
    }


    public static void main(String[] args) {
        ListNode l = ListTool.createListFromArray(new int[]{9, 7, 8, 5, 3, 1, 2});
        l = (new SortList_148()).sortList(l);
        ListTool.printList(l);


        //ListNode l = ListTool.createListFromArray(new int[]{2, 5, 6, 1, 4, 7});
        //ListNode mid = getMidNode(l, l.next.next.next.next.next);
        //ListNode hi = ListTool.getLastNode(l);

        //l = mergeList(l, mid, hi);
        //ListTool.printList(l);

    }


}

/**
 * 总结
 * 这个题目容易陷入链表指针调整混乱中.
 * 每个阶段都有固定的调整动作
 * 调整1: mergeSort的切分阶段, 中间节点需要和后半段链表断开, 这个阶段不需要考虑链表重连
 * 调整2: merge阶段, merge操作会把原来断开的链表重连
 */
