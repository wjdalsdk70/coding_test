import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class test2 {
    static class Point {
        int x, y;
        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    static int n;
    static int m;
    private static final int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public static void main(String[] args) throws IOException {
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();
        scanner.nextLine();

        char[][] grid = new char[n][m];
        Point start = null;
        Point exit = null;
        List<Point> ghosts = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            String line = scanner.nextLine();
            for (int j = 0; j < m; j++) {
                grid[i][j] = line.charAt(j);
                if (grid[i][j] == 'N') {
                    start = new Point(i, j);
                } else if (grid[i][j] == 'D') {
                    exit = new Point(i, j);
                } else if (grid[i][j] == 'G') {
                    ghosts.add(new Point(i, j));
                }
            }
        }

        if (canEscape(grid, start, exit, ghosts)) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }

    private static boolean canEscape(char[][] grid, Point start, Point exit, List<Point> ghosts) {
        boolean[][] threatened = new boolean[n][m];
        Queue<Point> queue = new LinkedList<>();

        for (Point ghost : ghosts) {
            queue.add(ghost);
            threatened[ghost.x][ghost.y] = true;
        }

        while (!queue.isEmpty()) {
            Point current = queue.poll();
            for (int[] dir : directions) {
                int nx = current.x + dir[0];
                int ny = current.y + dir[1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !threatened[nx][ny] && grid[nx][ny] != '#' && grid[nx][ny] != 'D') {
                    threatened[nx][ny] = true;
                    queue.add(new Point(nx, ny));
                }
            }
        }

        // Start BFS from 'N' to find a path to 'D'
        queue.add(start);
        boolean[][] visited = new boolean[n][m];
        visited[start.x][start.y] = true;

        while (!queue.isEmpty()) {
            Point current = queue.poll();
            if (current.x == exit.x && current.y == exit.y) {
                return true;
            }
            for (int[] dir : directions) {
                int nx = current.x + dir[0];
                int ny = current.y + dir[1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny] && !threatened[nx][ny] && grid[nx][ny] != '#') {
                    visited[nx][ny] = true;
                    queue.add(new Point(nx, ny));
                }
            }
        }

        return false;
    }
}
