package problems;

import tools.TreeTool;

public class MergeTwoBinaryTrees_617 {
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        if (t1 != null && t2 != null) {
            t1.val += t2.val;
        } else {
            return t1 != null ? t1 : t2;
        }

        if (t1.left == null && t2.left != null) {
            t1.left = t2.left;
            return t1;
        }

        if (t1.right == null && t2.right != null) {
            t1.right = t2.right;
            return t1;
        }

        mergeTrees(t1.left, t2.left);
        mergeTrees(t1.right, t2.right);

        return t1;
    }

    public static void main(String[] args) {
        TreeNode t1 = TreeTool.createTreeFromArray(new Integer[]{1, 3, 2, 5, null, null, null});
        TreeNode t2 = TreeTool.createTreeFromArray(new Integer[]{2, 1, 3, null, 4, null, 7});
        TreeNode t = (new MergeTwoBinaryTrees_617()).mergeTrees(t1, t2);
        TreeTool.printTree(t);


        t1 = TreeTool.createTreeFromArray(new Integer[]{1});
        t2 = TreeTool.createTreeFromArray(new Integer[]{});
        t = (new MergeTwoBinaryTrees_617()).mergeTrees(t1, t2);
        TreeTool.printTree(t);
    }
}
