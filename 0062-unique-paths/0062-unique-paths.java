class Solution {
    public int uniquePaths(int m, int n) {
        // Space optimized to O(n) - only store current row
        int dp[] = new int[n];
        // Initialize first row
        for(int j=0;j<n;j++)
            dp[j]=1;

        for(int i=1;i<m;i++){
            for(int j=1;j<n;j++){
                // dp[j] represents current cell
                // dp[j] (before update) represents cell above (previous row)
                // dp[j-1] represents cell to the left (current row)
                dp[j] = dp[j] + dp[j-1];
            }
        }
        return dp[n-1];
    }
}