import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class t5 {
    static class Point {
        int x, y, cnt;
        Point(int x, int y, int c) {
            this.x = x;
            this.y = y;
            this.cnt = c;
        }
    }
    static int h;
    static int w;
    static int[][] grid;
    static boolean[][] visited;
    static int max_cnt = 0;
    private static final int[][] directions = {{-1, 2}, {-2, 1}, {-1, -2}, {-2,-1},{1,2},{1,-2},{2,1},{2,-1}};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        h = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());
        grid = new int[h][w];
        bfs();
        if(isAllSearch()){
            System.out.println("T" +max_cnt);
        }else{
            System.out.println("F"+ max_cnt);
        }

    }

    private static boolean isAllSearch() {
        boolean jd = true;
        for (boolean[] booleans : visited) {
            for (boolean aBoolean : booleans) {
                if (!aBoolean) jd = false;
            }
        }
        return jd;
    }

    static void bfs(){
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(0,0,0));
        visited = new boolean[h][w];
        visited[0][0] = true;

        while (!q.isEmpty()) {
            Point current = q.poll();
            if(max_cnt < current.cnt) max_cnt = current.cnt;
            for (int[] dir : directions) {
                int nx = current.x + dir[0];
                int ny = current.y + dir[1];
                if (nx >= 0 && nx < h && ny >= 0 && ny < w && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    q.add(new Point(nx, ny, current.cnt+1));
                }
            }
        }
    }
}
