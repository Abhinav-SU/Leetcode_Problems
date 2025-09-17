class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int downone = 0;
        int downtwo = 0;
        for(int i = 2; i<=cost.length;i++){
            int temp = downone;
            downone = Math.min(downone+cost[i-1],downtwo+cost[i-2]);
            downtwo = temp;
        }
        return downone;
    }
}