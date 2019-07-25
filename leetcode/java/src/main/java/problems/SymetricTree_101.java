package problems;

public class SymetricTree_101 {

    public boolean isSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }

        return this.checkTree(root.left, root.right);
    }

    private boolean checkTree(TreeNode nodeLeft, TreeNode nodeRight) {
        if (nodeLeft == null && nodeRight == null) {
            return true;
        }else if (nodeLeft != null && nodeRight != null) {
            if (nodeLeft.val == nodeRight.val) {
                return this.checkTree(nodeLeft.left, nodeRight.right) && this.checkTree(nodeLeft.right, nodeRight.left);
            }
        }

        return false;
    }
}
