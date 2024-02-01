public class Solution {
    public int[][] divideArray(int[] nums, int k) {
        Arrays.sort(nums);
        List<int[]> resultList = new ArrayList<>();

        for (int i = 0; i + 2 < nums.length; i += 3) {
            if (nums[i + 2] - nums[i] <= k) {
                int[] triplet = Arrays.copyOfRange(nums, i, i + 3);
                resultList.add(triplet);
            } else {
                return new int[0][0];
            }
        }

        return resultList.toArray(new int[0][]);
    }
}
