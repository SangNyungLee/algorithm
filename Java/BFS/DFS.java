import java.util.*;
import java.io.*;

public class DFS {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());

        boolean [][]graph = new boolean[n + 1][n + 1];
        boolean [] visited = new boolean[n + 1];

        for(int i = 0 ; i < m ; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a][b] = true;
            graph[b][a] = true;
        }
        dfs(v, graph, visited, n, bw);
        bw.newLine();

        visited = new boolean[n + 1];
        bfs(v, graph, visited, n, bw);

        bw.flush();
        bw.close();
    }
    static void bfs(int start, boolean[][]graph, boolean[] visited, int n, BufferedWriter bw) throws IOException {
        StringBuilder sb = new StringBuilder();
        Queue<Integer> queue = new LinkedList<>();
        visited[start] = true;
        queue.offer(start);
        while(!queue.isEmpty()){
            int cur = queue.poll();
            bw.write(cur + " ");
            for(int i = 1 ; i < n + 1 ; i++){
                if (!visited[i] && graph[cur][i]){
                    queue.offer(i);
                    visited[i] = true;
                }
            }
        }
    }

    static void dfs(int start, boolean[][] graph , boolean[] visited, int n, BufferedWriter bw) throws IOException{
        visited[start] = true;
        bw.write(start + " ");
        for(int i = 1 ; i < n + 1 ; i++){
            if (!visited[i] && graph[start][i]){
                dfs(i, graph, visited, n, bw);
            }
        }
    }
}
