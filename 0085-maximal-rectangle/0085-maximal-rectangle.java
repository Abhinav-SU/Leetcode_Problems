class Solution {
    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }

        int maxArea = 0;
        int dp[] = new int [matrix[0].length];

        for(int i = 0; i< matrix.length; i++){
            for(int j =0; j< matrix[0].length; j++){
                dp[j] = matrix[i][j] =='1' ? dp[j]+1 : 0;
            }
            maxArea = Math.max(maxArea , maxHistogram(dp));
        }
       
        return maxArea;
    }

    public int maxHistogram(int dp[]){
        Stack<int[]> stack = new Stack<>();
        int n = dp.length;
        int maxArea = 0;

        for(int i = 0;i < n ; i++ ){
            int h =dp[i];
            int start = i;
            while(!stack.isEmpty() && stack.peek()[1] > h){
                int popped[] = stack.pop();
                int index = popped[0];
                int height = popped[1];
                maxArea = Math.max(maxArea , height * (i - index));
                start = index;
            }
            stack.push(new int[]{start, h});
        }

        while(!stack.isEmpty()){
            int popped[] = stack.pop();
            int index = popped[0];
            int height = popped[1];
            maxArea = Math.max(maxArea , height * (dp.length - index));
        }
        return maxArea;
    }
}