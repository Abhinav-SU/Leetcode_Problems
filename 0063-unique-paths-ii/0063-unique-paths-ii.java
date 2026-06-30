class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m =obstacleGrid.length;
        int n =obstacleGrid[0].length;
        if(obstacleGrid[0][0]==1 || obstacleGrid[m-1][n-1]==1)
            return 0;
        
        // Space optimized to O(n) - only store current row
        int dp[] = new int[n];
        dp[0]=1;
        
        // Initialize first row
        for(int i=1;i<n;i++){
            if(obstacleGrid[0][i]==1)
                dp[i]=0;
            else
                dp[i]=dp[i-1];
        }
        
        for(int i=1;i<m;i++){
            // Handle first column for current row
            if(obstacleGrid[i][0]==1)
                dp[0]=0;
            
            for(int j=1;j<n;j++){
                if(obstacleGrid[i][j]==1){
                    dp[j]=0;
                }
                else{
                    // dp[j] (before update) = cell above
                    // dp[j-1] = cell to the left
                    dp[j] = dp[j] + dp[j-1];
                }
            }
        }
        return dp[n-1];
    }
}