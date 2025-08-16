import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    static int N;
    static int[][] matrix;
    static boolean[][] visited;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        matrix = new int[N][N];
        visited = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < N; j++) {
                matrix[i][j] = Integer.parseInt(s[j]);
            }
        }

        List<Integer> areaSizes = new ArrayList<>();
        // 각 영역의 크기 구하기
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (matrix[i][j] == 1 && !visited[i][j]) {
                    int areaSize = bfs(i, j);
                    areaSizes.add(areaSize);
                }
            }
        }

        // 영역 크기 오름차순 정렬
        Collections.sort(areaSizes);

        // 결과 출력
        System.out.println(areaSizes.size());
        for (int size : areaSizes) {
            System.out.print(size + " ");
        }
    }

    public static int bfs ( int x, int y){
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{x, y});
        visited[x][y] = true;
        int areaSize = 1;

        while (!q.isEmpty()) {
            int[] current = q.poll();
            int cx = current[0];
            int cy = current[1];

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if (nx >= 0 && ny >= 0 && nx < N && ny < N && matrix[nx][ny] == 1 && !visited[nx][ny]) {
                    q.offer(new int[]{nx, ny});
                    visited[nx][ny] = true;
                    areaSize++;
                }
            }
        }
        return areaSize;
    }
}

