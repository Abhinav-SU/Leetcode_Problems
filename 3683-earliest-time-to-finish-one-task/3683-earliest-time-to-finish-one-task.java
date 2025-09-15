class Solution {
    public int earliestTime(int[][] tasks) {
        int len = tasks.length;
        int earliest =Integer.MAX_VALUE;
        for(int[] task: tasks){
            int curr_time = task[0]+task[1];
            if(curr_time < easrliest)
                earliest = curr_time;
        }
        return earliest;
    }
}