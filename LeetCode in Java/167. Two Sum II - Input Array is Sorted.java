class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int desired, lo=0, hi=numbers.length-1;
        int[] ans = new int[2];
        while(lo < hi){
            int sum = numbers[lo]+numbers[hi];
            if(sum == target){
                ans[0]=lo+1;
                ans[1]=hi+1;
                break;
            }
            else if(sum < target) lo++;
            else hi--;
        }
        return ans;
    }
}
