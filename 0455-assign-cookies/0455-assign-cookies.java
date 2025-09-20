class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int contentChildren =0;
        int index=0;

        while(index<s.length && contentChildren <g.length){
            if(g[contentChildren]<=s[index]){
                contentChildren++;
            }
            index++;
        }
        return contentChildren;
    }
}