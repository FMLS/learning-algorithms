package problems;

public class EasyString {

    public static void PrcStr(String s) {
        char[] as = s.toCharArray();

        int i = 0;
        while (i < as.length) {
            int j = i + 1;
            while (j < as.length && as[j] == as[i]) {
                j++;
            }
            if (j - i == 1) {
                System.out.print(as[i]);
            }
            i = j;
        }
    }

    public static void main(String[] args) {
        String s = "abcccdefghhhij";
        EasyString.PrcStr(s);
    }
}
