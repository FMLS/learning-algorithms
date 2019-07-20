package problems;

public class UnivaluedBinaryTree_965 {
    public boolean isUnivalTree(TreeNode root) {
        boolean isLeft = true;
        if (root.left != null) {
            if (root.left.val != root.val) {
                return false;
            }
            isLeft = isUnivalTree(root.left);
        }

        if (!isLeft) {
            return false;
        }

        boolean isRight = true;
        if (root.right != null) {
            if (root.right.val != root.val) {
                return false;
            }
            isRight = isUnivalTree(root.right);
        }

        return isRight;
    }
}
