package problems;

import tools.TreeTool;

/**
 * Given two binary trees, write a function to check if they are the same or not.
 *
 * Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
 */


public class SameTree_100 {

    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        else if ((p == null && q != null) || (p != null && q == null)) return false;
        else {
            if (p.val != q.val) return false;
            return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        }
    }


    public static void main(String[] args) {
        TreeNode t1 = TreeTool.createTreeFromArray(new Integer[]{1, 2, 3});
        TreeNode t2 = TreeTool.createTreeFromArray(new Integer[]{1, 2, 3});
        boolean x = (new SameTree_100()).isSameTree(t1, t2);
        System.out.println(x);


        t1 = TreeTool.createTreeFromArray(new Integer[]{1, 2, });
        t2 = TreeTool.createTreeFromArray(new Integer[]{1, null, 2});
        x = (new SameTree_100()).isSameTree(t1, t2);
        System.out.println(x);
    }
}
