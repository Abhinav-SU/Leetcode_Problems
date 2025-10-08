class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] dp = new int[n][2];
        
        // Initialize dp with a sentinel value
        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], Integer.MIN_VALUE);
        }
        
        return f(0, 1, prices, dp);
    }

    public int f(int indx, int buy, int[] prices, int[][] dp) {
        if (indx == prices.length)
            return 0;
        
        if (dp[indx][buy] != Integer.MIN_VALUE) 
            return dp[indx][buy];
        
        int profit = 0;
        if (buy == 1) {
            // Option to buy or skip
            profit = Math.max(-prices[indx] + f(indx + 1, 0, prices, dp), 
                              f(indx + 1, 1, prices, dp));
        } else {
            // Option to sell or skip
            profit = Math.max(prices[indx] + f(indx + 1, 1, prices, dp), 
                              f(indx + 1, 0, prices, dp));
        }
        
        return dp[indx][buy] = profit;
    }
}
