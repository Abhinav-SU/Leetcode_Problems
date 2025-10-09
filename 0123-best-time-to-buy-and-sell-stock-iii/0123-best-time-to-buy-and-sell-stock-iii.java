class Solution {
    public int maxProfit(int[] prices) {
        int S1_Profit = 0, B1_Profit = Integer.MIN_VALUE; // Transaction 1 states
    int S2_Profit = 0, B2_Profit = Integer.MIN_VALUE; // Transaction 2 states
        for (int price : prices) {

                    // Transaction 1 updates (must use results from Transaction 0 = 0)
        S1_Profit = Math.max(S1_Profit, B1_Profit + price); // Sell 1 (based on B1)
        B1_Profit = Math.max(B1_Profit, -price); 
        // Transaction 2 updates (must use results from Transaction 1)
        S2_Profit = Math.max(S2_Profit, B2_Profit + price); // Sell 2 (based on B2)
        B2_Profit = Math.max(B2_Profit, S1_Profit - price); // Buy 2 (based on S1)
        
           // Buy 1 (based on 0 profit)
    }            
    return S2_Profit;
    }
}