package tools;

import problems.TreeNode;

import java.util.*;

public class TreeTool {

    public static void printTree(TreeNode head) {
        System.out.println("Binary Tree:");
        printInOrder(head, 0, "H", 17);
        System.out.println();
    }

    private static void printInOrder(TreeNode head, int height, String to, int len) {
        if (head == null) {
            return;
        }
        printInOrder(head.right, height + 1, "v", len);
        String val = to + head.val + to;
        int lenM = val.length();
        int lenL = (len - lenM) / 2;
        int lenR = len - lenM - lenL;
        val = getSpace(lenL) + val + getSpace(lenR);
        System.out.println(getSpace(height * len) + val);
        printInOrder(head.left, height + 1, "^", len);
    }

    public static String getSpace(int num) {
        String space = " ";
        StringBuffer buf = new StringBuffer("");
        for (int i = 0; i < num; i++) {
            buf.append(space);
        }
        return buf.toString();
    }

    public static TreeNode createTreeFromArray(Integer[] a) {
        if (a.length == 0) return null;
        LinkedList<Integer> l = new LinkedList<>(Arrays.asList(a));
        TreeNode head = new TreeNode(l.pop());
        LinkedList<TreeNode> queue = new LinkedList<>();
        queue.add(head);

        TreeNode p, left, right;

        for (int i = 1; i < a.length;) {
            p = queue.pop();
            left = right = null;
            if (a[i] != null) {
                left = new TreeNode(a[i]);
            }
            i++;

            if (i < a.length && a[i] != null) {
                right = new TreeNode(a[i]);
            }
            i++;

            p.left = left;
            p.right = right;

            queue.add(left);
            queue.add(right);
        }

        return head;
    }

    public static void main(String[] args) {
        TreeNode tree = createTreeFromArray(new Integer[]{10, 5, 15, 3, 7, null, 18});
        printTree(tree);
        tree = createTreeFromArray(new Integer[]{10, 5, 15, 3, 7, 13, 18, 1, null, 6});
        printTree(tree);
    }
}
