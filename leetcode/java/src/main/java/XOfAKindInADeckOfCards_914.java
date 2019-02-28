import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class XOfAKindInADeckOfCards_914 {

    private int gcd(int a, int b) {
        return b > 0 ? gcd(b, a % b) : a;
    }

    public boolean hasGroupsSizeX(int[] deck) {
        HashMap<Integer, Integer> h = new HashMap<>();
        for (int i : deck) {
            Integer res = h.get(i);
            if (res != null) {
                h.put(i, ++res);
            } else {
                h.put(i, 1);
            }
        }

        int res = 0;
        for (int item : h.values()) {
            res = gcd(item, res);
        }

        return res > 1;
    }
}
