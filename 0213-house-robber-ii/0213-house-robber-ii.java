class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
    if (n == 0) return 0;
    if (n == 1) return nums[0];

    int[] dp1 = new int[n + 1];
    int[] dp2 = new int[n + 1];

    dp1[0] = 0;
    dp1[1] = nums[0]; // include first
    dp2[0] = 0;
    dp2[1] = 0;       // exclude first

    // Case 1: include first, exclude last
    for (int i = 2; i <= n - 1; i++) {
        dp1[i] = Math.max(dp1[i - 1], dp1[i - 2] + nums[i - 1]);
    }

    // Case 2: exclude first, include last
    for (int i = 2; i <= n; i++) {
        dp2[i] = Math.max(dp2[i - 1], dp2[i - 2] + nums[i - 1]);
    }

    return Math.max(dp1[n - 1], dp2[n]);
    }
}