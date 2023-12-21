
class Solution {
    public int maxWidthOfVerticalArea(int[][] points) {
        Arrays.sort(points, (a, b) -> a[0] - b[0]);

        int maxWidth = 0;
        for (int i = 0; i < points.length - 1; i++) {
            maxWidth = Math.max(maxWidth, points[i + 1][0] - points[i][0]);
        }

        return maxWidth;
    }
}
