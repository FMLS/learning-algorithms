import org.junit.Test;
import org.junit.Before;
import org.junit.After;

/**
 * BestTimeToBuyAndSellStockII_122 Tester.
 *
 * @author <Authors name>
 * @since <pre>Jan 14, 2019</pre>
 * @version 1.0
 */
public class BestTimeToBuyAndSellStockII_122Test {

    @Before
    public void before() throws Exception {
    }

    @After
    public void after() throws Exception {
    }

    /**
     *
     * Method: maxProfit(int[] prices)
     *
     */
    @Test
    public void testMaxProfit() throws Exception {
        int[] data = {7, 1, 5, 3, 6, 4};
        BestTimeToBuyAndSellStockII_122 solution = new BestTimeToBuyAndSellStockII_122();
        int res = solution.maxProfit(data);
        System.out.println(res);
    }


} 
