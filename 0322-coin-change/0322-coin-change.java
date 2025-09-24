class Solution {
    public int coinChange(int[] coins, int amount) {
        //save the state of all the min number of coins leading upto amount
        int dp[] = new int[amount+1];
        Arrays.fill(dp,amount+1);
        //number of coins needed to maker the amount 0 and also our base case
        dp[0]=0;
        //for each sate save the min number of coins 
        for(int i=1 ; i<=amount;i++){
            //iterate through coins array
            for(int j=0;j<coins.length;j++){
                if(coins[j]<=i){
                     dp[i] = Math.min(dp[i],dp[i-coins[j]]+1);
                     }
               
            }
        }
        return dp[amount] >amount ? -1 : dp[amount];
    }
}