import java.util.Deque;
import java.util.ArrayDeque;
class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        if (image[sr][sc] == color) {
            return image;
        }
        int n = image.length;
        int m = image[0].length;
        int orColor = image[sr][sc];
        int dire[][] = {{0,1},{0,-1},{1,0},{-1,0}};
        Deque<int []>stack = new ArrayDeque<>();
        stack.push(new int[]{sr,sc});
        image[sr][sc] = color;
        
        while(!stack.isEmpty()){
            int []cur = stack.pop();
            for(int[] dir:dire){
                int nr = cur[0]+dir[0];
                int nc = cur[1]+dir[1];
                if(nr >= 0 && nr < n && nc >=0 && nc <m && image[nr][nc]==orColor){
                    image[nr][nc]=color;
                    stack.push(new int[]{nr,nc});
                }
            }

        }
        return image;
    }
}