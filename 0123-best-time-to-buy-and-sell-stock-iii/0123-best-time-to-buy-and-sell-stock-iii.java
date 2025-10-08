class Solution {
    public int maxProfit(int[] prices) {
        int t1buy = Integer.MAX_VALUE,t2buy =Integer.MAX_VALUE;
        int t1profit = 0, t2profit =0;

        for(int price : prices){
            t1buy = Math.min(t1buy, price);
            t1profit = Math.max(t1profit,price-t1buy);
            t2buy = Math.min(t2buy,price-t1profit);
            t2profit = Math.max(t2profit,price-t2buy);
        }
        return t2profit;
    }
}