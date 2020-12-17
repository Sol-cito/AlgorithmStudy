import java.util.Scanner;

public class q_1987 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] input = sc.nextLine().split(" ");
        int R = Integer.parseInt(input[0]);
        int C = Integer.parseInt(input[1]);
        int[][] arr = new int[R][C];
        for (int i = 0; i < R; i++) {
            char[] ip = sc.nextLine().toCharArray();
            for (int j = 0; j < ip.length; j++) {
                arr[i][j] = ip[j] - 65;
            }
        }
        int[] ascii = new int[27];
        int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        ascii[arr[0][0]] = 1;
        System.out.println(recursion(arr, 0, 0, 1, ascii, directions));
    }

    public static int recursion(int[][] arr, int x, int y, int num, int[] ascii, int[][] directions) {
        if (num == 26) return 26;
        int temp = 0;
        for (int i = 0; i < directions.length; i++) {
            int nx = x + directions[i][0];
            int ny = y + directions[i][1];
            if (0 <= nx && nx < arr.length && 0 <= ny && ny < arr[0].length && ascii[arr[nx][ny]] == 0) {
                int ori = arr[nx][ny];
                ascii[ori] = 1;
                temp = Math.max(temp, recursion(arr, nx, ny, num + 1, ascii, directions));
                ascii[ori] = 0;
            }
        }
        return Math.max(num, temp);
    }
}
