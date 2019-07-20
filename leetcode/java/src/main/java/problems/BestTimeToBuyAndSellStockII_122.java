package problems;

public class BestTimeToBuyAndSellStockII_122 {
    public int maxProfit(int[] prices) {

        int sum = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            if (prices[i] < prices[i + 1]) {
               sum += prices[i + 1] - prices[i];
            }
        }

        return sum;
    }

    public static void main(String[] args) {
        int[] data = {7, 1, 5, 3, 6, 4};
        BestTimeToBuyAndSellStockII_122 solution = new BestTimeToBuyAndSellStockII_122();
        int res = solution.maxProfit(data);
        System.out.println(res);
    }

}
