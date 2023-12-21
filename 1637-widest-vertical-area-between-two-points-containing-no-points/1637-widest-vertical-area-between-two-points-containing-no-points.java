class Solution {
    public int maxWidthOfVerticalArea(int[][] points) {
        int[] xSorted = Arrays.stream(points).mapToInt(point -> point[0]).sorted().toArray();

        int maxWidth = 0;
        for (int i = 0; i < xSorted.length - 1; i++) {
            maxWidth = Math.max(maxWidth, xSorted[i + 1] - xSorted[i]);
        }

        return maxWidth; 
    }
}