package problems;

/**
 * Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
 *
 * Note: For the purpose of this problem, we define empty string as valid palindrome.
 *
 * Example 1:
 *
 * Input: "A man, a plan, a canal: Panama"
 * Output: true
 * Example 2:
 *
 * Input: "race a car"
 * Output: false
 */


/**
 * 这道题corner case比较多, 写了很多if else也没写对, 思路不够清晰, 下面leetcode discuss比较好的答案
 */
public class ValidPalindrome_125 {
    /*
    正则表达式法
     */
    //public boolean isPalindrome(String s) {
    //    String actual = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
    //    String reverse = new StringBuffer(actual).reverse().toString();
    //    return actual.equals(reverse);
    //}


    /*
    双指针法
     */

    public boolean isPalindrome(String s) {
        if (s.isEmpty()) {
            return true;
        }
        int head = 0, tail = s.length() - 1;
        char cHead, cTail;
        while(head <= tail) {
            cHead = s.charAt(head);
            cTail = s.charAt(tail);
            if (!Character.isLetterOrDigit(cHead)) {
                head++;
            } else if(!Character.isLetterOrDigit(cTail)) {
                tail--;
            } else {
                if (Character.toLowerCase(cHead) != Character.toLowerCase(cTail)) {
                    return false;
                }
                head++;
                tail--;
            }
        }

        return true;
    }

    //private boolean valid(String s) {
    //    return (s.compareTo("a") >= 0 && s.compareTo("z") <= 0) || (s.compareTo("A") >= 0 && s.compareTo("Z") <= 0) || (s.compareTo("0") >= 0 && s.compareTo("9") <= 0);
    //}

    public static void main(String[] args) {
        boolean res = (new ValidPalindrome_125()).isPalindrome("A man, a plan, a canal: Panama");
        System.out.println(res);
        res = (new ValidPalindrome_125()).isPalindrome("");
        System.out.println(res);
        res = (new ValidPalindrome_125()).isPalindrome("aba");
        System.out.println(res);
        res = (new ValidPalindrome_125()).isPalindrome(",.");
        System.out.println(res);
        res = (new ValidPalindrome_125()).isPalindrome("a,");
        System.out.println(res);
        res = (new ValidPalindrome_125()).isPalindrome(".,");
        System.out.println(res);
    }
}
