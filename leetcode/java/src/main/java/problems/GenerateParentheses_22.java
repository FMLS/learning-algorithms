package problems;

import com.sun.tools.javac.jvm.Gen;

import java.util.ArrayList;
import java.util.List;

public class GenerateParentheses_22 {
    public List<String> generateParenthesis(int n) {

        List<String> items = new ArrayList<>();
        this.doGen(n * 2 , 0, "", items);
        return items;
    }

    private void doGen(int n, int sum, String str, List<String> items) {
        if (sum < 0) {
            return;
        }

        if (n == 0) {
            if (sum == 0) {
                items.add(str);
            }
            return;
        }

        this.doGen(n - 1, sum + 1, str + "(", items);
        this.doGen(n - 1, sum - 1, str + ")", items);
    }

    public static void main(String[] args) {
        List<String> res = (new GenerateParentheses_22()).generateParenthesis(3);
        System.out.println(res);
    }
}
