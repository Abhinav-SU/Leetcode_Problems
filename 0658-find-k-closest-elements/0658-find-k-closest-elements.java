class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        int left = 0;
        int right = arr.length-k;
        List<Integer> result = new ArrayList<>();

        if(k==arr.length)
           {
            List<Integer> res = new ArrayList<>();
            for (int num : arr) res.add(num);
                return res;
           }

        while(left<right){
            int mid = (left+right)/2;
            if(x-arr[mid]>arr[mid+k]-x){
                left = mid+1;}
            else{
                right =mid; 
                }
        }
        for(int i=left;i<=left+k;i++){
            result.add(arr[i]);
        }
        return result;
    }
}