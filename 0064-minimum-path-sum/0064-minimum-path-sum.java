class Solution {
    public int minPathSum(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        
        // Space optimized to O(m) - only store current row
        int dp[] = new int[m];
        dp[0] = grid[0][0];
        
        // Initialize first row
        for(int j=1; j<m; j++){
            dp[j] = dp[j-1] + grid[0][j];
        }
        
        for(int i=1; i<n; i++){
            // Update first column for current row
            dp[0] = dp[0] + grid[i][0];
            
            for(int j=1; j<m; j++){
                // dp[j] (before update) = cell above
                // dp[j-1] = cell to the left
                dp[j] = grid[i][j] + Math.min(dp[j], dp[j-1]);
            }
        }
        return dp[m-1];
    }
}