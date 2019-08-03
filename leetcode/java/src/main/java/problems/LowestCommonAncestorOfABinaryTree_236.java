package problems;

/**
 * Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
 * According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
 *
 *
 * 这个题目的思路主要在于三点:
 * 1 利用递归后序遍历, 收集左右子树结果
 * 2 递归结束条件的选择
 * 3 递归返回时, 返回节点的选择, 主要不好想到的是当一边为空, 另一边不是空, 无论不为空的节点是不是我们要找的那个节点, 都直接向上返回, 如果是我们要找的节点, 则到
 * 根节点时另一边一定是空, 这样一边是空另一边不是空, 则返回非空节点就可得到正确结果
 */
public class LowestCommonAncestorOfABinaryTree_236 {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) return null;
        if (root == p) return p;
        if (root == q) return q;

        TreeNode resLeft = this.lowestCommonAncestor(root.left, p, q);
        TreeNode resRight = this.lowestCommonAncestor(root.right, p, q);

        //if (resLeft != null && resRight != null)
        //    return root;
        //else if (resLeft != null) {
        //    return resLeft;
        //} else if (resRight != null) {
        //    return resRight;
        //} else {
        //    return null;
        //}

        // 上面的代码可以用这行代替, 但明显可读性不强
        if (resLeft != null && resRight != null) {
            return root;
        }
        return resLeft != null ? resLeft : resRight;
    }
}
