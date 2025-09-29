class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        if(text1.length()==0 || text2.length()==0)
            return 0;
        if(text2.length() < text1.length()){
            String temp = text1;
            text1 =text2;
            text2 =temp;
        }

        int current[] = new int[text1.length()+1];
        int previous[] = new int[text1.length()+1];

        for(int col = text2.length()-1; col>=0 ;col--){
            for(int row = text1.length()-1;row>=0;row--){
                if(text1.charAt(row)==text2.charAt(col)){
                    current[row]=1+previous[row+1];
                }
                else{
                    current[row]=Math.max(previous[row],current[row+1]);
                }
            }
            int[] temp = previous;
            previous = current;
            current = temp;
        }
        return previous[0];
    }
}